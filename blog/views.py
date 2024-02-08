from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower


from .models import BlogPost


def blog_posts(request):
    """ 
    A view to show all blogposts. Also 
    includes sorting and search queries.
    """
    blog_posts = BlogPost.objects.all()

    query = None
    sort = None
    direction = None

    # Sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            blog_posts = blog_posts.annotate(lower_name=Lower('title'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        blog_posts = blog_posts.order_by(sortkey)

    for blog_post in blog_posts:
        if blog_post.reviews_average is not None:
            blog_post.reviews_average = round(blog_post.reviews_average)

    # Queries
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter anything to search")
                return redirect(reverse('blog_posts'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            blog_posts = blog_posts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    def total_blog_posts_number():
        """ 
        A function to return the total number of blog_posts
        """
        total_blog_posts = blog_posts.count()
        return total_blog_posts

    context = {
        'blog_posts': blog_posts,
        'search_term': query,
        'current_sorting': current_sorting,
        'total_blog_posts_number': total_blog_posts_number,
    }

    return render(request, 'blog/blog_posts.html', context)


def blog_post_detail(request, id):
    """ 
    A view to show a specific blog post.
    """
    blog_post = get_object_or_404(BlogPost, pk=id)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)
