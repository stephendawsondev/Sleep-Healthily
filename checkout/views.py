from django.shortcuts import render


def view_checkout(request):
    """ A view that renders the checkout page """

    return render(request, 'checkout/checkout.html')
