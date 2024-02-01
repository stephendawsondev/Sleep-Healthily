from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ A view to show all products. Also 
    includes sorting and search queries.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product/products.html', context)


def product_detail(request, id):
    """ 
    A view to show a specific product.
    """
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)
