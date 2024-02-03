from django.shortcuts import (
    render, redirect, get_object_or_404, reverse
)
from django.contrib import messages
from product.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """
    View that handles adding products to the cart.
    """
    product = get_object_or_404(Product, pk=id)
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if id in list(cart.keys()):
        cart[id] += int(quantity)
        messages.success(request,
                         f'Updated {product.name} quantity to {cart[id]}')
    else:
        cart[id] = int(quantity)
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                             f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request,
                         (f'Removed {product.name} '
                             f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
