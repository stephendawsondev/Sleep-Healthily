from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)
from django.contrib import messages
from django.conf import settings

from product.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe
import json


def view_checkout(request):
    """ A view that renders the checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, f"""
                        Product {product.name} is no longer available
                        """
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with the form. \
                           Please check your inputs again.")

    else:
        if not cart:
            return redirect(reverse('products'))
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        total = current_cart['cart_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, ('Stripe public key not found. '
                                       'Did you forget to set it in '
                                       'your environment variables?'))

        template = 'checkout/checkout.html'

        context = {
            'order_form': order_form,
            'on_checkout_page': True,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)
