from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def products(request):
    """ 
    A view to show all products. Also 
    includes sorting and search queries.
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter anything to search")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
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
