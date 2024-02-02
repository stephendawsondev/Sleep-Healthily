from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    cart_total = 0

    if subtotal < settings.FREE_SHIPPING_THRESHOLD:
        shipping = subtotal * \
            Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_remainder = settings.FREE_SHIPPING_THRESHOLD - subtotal
    else:
        shipping = 0
        free_shipping_remainder = 0

    cart_total = shipping + subtotal

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'cart_total': cart_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_remainder': free_shipping_remainder,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
    }

    return context
