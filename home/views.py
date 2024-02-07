from django.shortcuts import render
from product.models import Product


def index(request):
    """ A view to return the index page """

    featured_product = Product.objects.all()[0]

    context = {
        'featured_product': featured_product,
    }

    return render(request, 'home/index.html', context)
