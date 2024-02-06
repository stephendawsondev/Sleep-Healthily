from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Review
from product.models import Product

from .forms import ReviewForm


@login_required
def create_review(request, product_id):
    """
    View to create a review on a product page. The
    review is created using the form data and saved
    to the database. It can only be created by a user
    who is logged in and has purchased the product.
    """
    product = Product.objects.get(id=product_id)
    user = request.user

    form = ReviewForm()

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review(
            product=product,
            user=user,
            title=title,
            text=text,
            rating=rating
        )
        review.save()
        return redirect('product_detail', product_id)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'review/create_review.html', context)


def helpful_votes(request, review_id):
    """
    View to toggle helpful votes on a review. If the 
    user has already voted, the vote is removed. If the
    user hasn't voted, the vote is added.
    """
    review = Review.objects.get(id=review_id)
    user = request.user
    if user in review.helpful_votes.all():
        review.helpful_votes.remove(user)
    else:
        review.helpful_votes.add(user)
    return redirect('product_detail', review.product.id)
