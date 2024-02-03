from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from product.models import Product


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    cart_total = 0
    cart = request.session.get('cart', {})
    free_shipping = False

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal += quantity * product.price
        product_count += quantity
        line_total = product.price * quantity
        cart_items.append({
            'id': item_id,
            'quantity': quantity,
            'line_total': line_total,
            'product': product,
        })

    if subtotal < settings.FREE_SHIPPING_THRESHOLD:
        shipping = subtotal * \
            Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_remainder = settings.FREE_SHIPPING_THRESHOLD - subtotal
    else:
        shipping = 0
        free_shipping_remainder = 0
        free_shipping = True

    cart_total = shipping + subtotal

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'cart_total': cart_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_remainder': free_shipping_remainder,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'free_shipping': free_shipping,
    }

    return context
