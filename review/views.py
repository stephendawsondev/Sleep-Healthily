from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    user_profile = user.userprofile

    # checking if the user has any orders, because
    # if they don't then there is no point continuing
    if not user_profile.orders.all():
        messages.error(
            request, "You must have purchased this product to review it.")
        return redirect('product_detail', product_id)

    # check if the user has orders and the product is in
    # one of the orders, if not then the user can't review
    orders = user_profile.orders.all()
    for order in orders:
        for item in order.line_items.all():
            if item.product == product:
                break
        else:
            messages.error(
                request, "You must have purchased this product to review it.")
            return redirect('product_detail', product_id)

    # check if the user has already reviewed the product
    # if they have, then they can't review it again
    review_exists = Review.objects.filter(product=product, user=user).exists()

    if review_exists:
        messages.error(
            request, "You have already reviewed this product, "
            "please update or delete your existing review.")
        return redirect('product_detail', product_id)

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

        messages.success(request, "Your review has been added.")
        return redirect('product_detail', product_id)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'review/create_review.html', context)


@login_required
def edit_review(request, review_id):
    """
    View to edit a review. The review is retrieved
    from the database and the form is pre-populated
    with the review data. The review is then updated
    and saved to the database.
    """
    review = Review.objects.get(id=review_id)
    product = review.product
    form = ReviewForm(initial={
        'title': review.title,
        'text': review.text,
        'rating': review.rating
    })

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review.title = title
        review.text = text
        review.rating = rating
        review.save()

        messages.success(request, "Your review has been updated.")
        return redirect('product_detail', product.id)

    context = {
        'product': product,
        'form': form,
        'review': review,
    }

    return render(request, 'review/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    View to delete a review. The review is retrieved
    from the database and then deleted.
    """
    review = Review.objects.get(id=review_id)
    product = review.product
    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('product_detail', product.id)


@login_required
def helpful_votes(request, review_id):
    """
    View to toggle helpful votes on a review. If the 
    user has already voted, the vote is removed. If the
    user hasn't voted, the vote is added.
    """
    review = Review.objects.get(id=review_id)
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You must be logged in to upvote.")
        return redirect('product_detail', review.product.id)

    if user in review.helpful_votes.all():
        review.helpful_votes.remove(user)
        messages.success(request, "You have removed your upvote.")
    else:
        review.helpful_votes.add(user)
        messages.success(request, "You have added your upvote.")

    return redirect('product_detail', review.product.id)
