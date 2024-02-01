from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product
from django.db.models.functions import Lower
from .forms import ProductForm


def products(request):
    """ 
    A view to show all products. Also 
    includes sorting and search queries.
    """
    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    # Sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    # Queries
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

    current_sorting = f'{sort}_{direction}'

    def total_products_number():
        """ 
        A function to return the total number of products
        """
        total_products = products.count()
        return total_products

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'total_products_number': total_products_number,
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


@login_required
def add_product(request):
    """ 
    Add a product to the store 
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'product/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
