from django.shortcuts import render
from product.models import Product
from review.models import Review


def index(request):
    """ A view to return the index page """

    featured_product = Product.objects.all()[0]
    reviews = Review.objects.filter(product=featured_product)
    reviews_count = reviews.count()
    reviews_average = 0
    if reviews_count > 0:
        reviews_total = 0
        for review in reviews:
            reviews_total += review.rating
        # round to 1 decimal place
        reviews_average = int(round(reviews_total / reviews_count, 1))

    context = {
        'featured_product': featured_product,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'reviews_average': reviews_average,
    }

    return render(request, 'home/index.html', context)
