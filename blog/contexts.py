from blog.models import BlogPost


def first_three_posts(request):
    """ A view to return featured blog posts. """
    featured_posts = BlogPost.objects.filter(
        status=1).order_by('-created_on')[:3]

    context = {
        'featured_posts': featured_posts
    }

    return context
