from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def view_checkout(request):
    """ A view that renders the checkout page """

    cart = request.session.get('cart', {})
    if not cart:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'on_checkout_page': True
    }

    return render(request, template, context)
