from django.shortcuts import (
    render, redirect, get_object_or_404
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

    print(request.session['cart'])
    return redirect(redirect_url)
