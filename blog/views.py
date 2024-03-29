from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from .models import BlogPost, Comment
from profiles.models import UserProfile

from .forms import BlogPostForm

User = get_user_model()


def get_user_full_name(user):
    """
    A function to get the full name of a user.
    """
    first_name = user.first_name
    last_name = user.last_name

    if first_name and last_name:
        full_name = f'{first_name} {last_name[0]}'
    else:
        full_name = user.username

    return full_name


def blog_post_detail(request, id):
    """
    A view to show a specific blog post.
    """
    blog_post = get_object_or_404(BlogPost, pk=id)
    comments = Comment.objects.filter(
        blog_post=blog_post)
    editing_comment_id = request.GET.get('editing_comment_id', None)

    if editing_comment_id:
        editing_comment_id = int(editing_comment_id)

    if blog_post.status == 0:
        if (
            not request.user.is_superuser
            and not request.user == blog_post.author.user
        ):
            messages.error(
                request, 'Sorry, this blog post is not available to view.'
            )
            return redirect(reverse('blog_posts'))

    author_name = get_user_full_name(blog_post.author.user)

    context = {
        'blog_post': blog_post,
        'author_name': author_name,
        'comments': comments,
        'editing_comment_id': editing_comment_id,
        'on_blog_page': True,
    }

    return render(request, 'blog/blog_post_detail.html', context)


def blog_posts(request):
    """
    A view to show all blog posts. Also
    includes sorting and search queries.
    """
    blog_posts = BlogPost.objects.all().filter(status=1)
    paginated = Paginator(blog_posts, 6)

    query = None
    sort = None
    direction = None

    # Sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'title':
            sortkey = 'lower_title'
            blog_posts = blog_posts.annotate(lower_title=Lower('title'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        blog_posts = blog_posts.order_by(sortkey)

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

    paginated = Paginator(blog_posts, 6)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)

    for blog_post in page.object_list:
        blog_post.author_name = get_user_full_name(blog_post.author.user)

    def total_blog_posts_number():
        """
        A function to return the total number of blog_posts
        """
        total_blog_posts = blog_posts.count()
        return total_blog_posts

    context = {
        'blog_posts': blog_posts,
        'page': page,
        'search_term': query,
        'current_sorting': current_sorting,
        'total_blog_posts_number': total_blog_posts_number,
        'on_blog_page': True,
    }

    return render(request, 'blog/blog_posts.html', context)


@login_required
def add_blog_post(request):
    """
    Add a blog post to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access that.')
        return redirect(reverse('blog_posts'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        user_profile = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = user_profile
            blog_post.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_post_detail', args=[blog_post.id]))
        else:
            messages.error(request,
                           ('Failed to add blog post. '
                            'Please ensure the form is valid.'))
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, id):
    """ Edit a blog post in the store """
    blog_post = get_object_or_404(BlogPost, pk=id)

    if not request.user.is_superuser and not request.user == BlogPost.author:
        messages.error(request, 'Only blog post owners can edit blog posts.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post')
            return redirect(reverse('blog_post_detail', args=[blog_post.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is filled out correctly.'))
    else:
        form = BlogPostForm(instance=blog_post)
        messages.info(request, f'You are editing {blog_post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, blog_post_id):
    """ Delete a blog post from the store """
    if not request.user.is_superuser and not request.user == BlogPost.author:
        messages.error(request, 'Only blog post owners can delete posts.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    blog_post.delete()
    messages.success(request, 'Blog post deleted')
    return redirect(reverse('blog_posts'))


@login_required
def favourite_blog_post(request, blog_post_id):
    """
    Add a blog post to the user's favourites
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    user = request.user

    if not user.is_authenticated:
        messages.error(
            request, "You must be logged in to favourite a blog post.")
        return redirect('blog_posts')

    if user.is_authenticated:
        if user.userprofile in blog_post.favourited.all():
            blog_post.favourited.remove(user.userprofile)
            messages.success(
                request, "You have removed this blog post from favourites.")
        else:
            blog_post.favourited.add(user.userprofile)
            messages.success(
                request, "You have added this blog post to your favourites.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_comment(request, blog_post_id):
    """
    A view to handle the submission of comments
    that are associated with a specific blog post.
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        author = user_profile
        content = request.POST['content']
        blog_post = blog_post
        comment = Comment(
            author=author,
            content=content,
            blog_post=blog_post
        )
        comment.save()

        messages.success(
            request, "Your comment is pending approval. It will appear "
            "once it has been approved by the blog post owner.")
    else:
        messages.error(request, "Failed to add comment. Please try again.")

    return redirect(reverse('blog_post_detail', args=[blog_post.id]))


@login_required
def edit_comment(request, comment_id):
    """
    A view to handle the editing of comments
    that are associated with a specific blog post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    blog_post = comment.blog_post
    comment_owner = comment.author.user

    if not request.user == comment_owner:
        messages.error(request, 'Only the comment owner can edit comments.')
        return redirect(reverse('blog_post_detail', args=[blog_post.id]))

    if request.method == 'POST':
        content = request.POST['content']
        comment.content = content
        comment.is_approved = False
        comment.save()

        messages.success(
            request, "Your comment has been updated and is pending approval.")
        return redirect(reverse('blog_post_detail', args=[blog_post.id]))

    comment_id = comment.id

    query_string = f"editing_comment_id={comment.id}"

    return redirect(
        f'{reverse("blog_post_detail", args=[blog_post.id])}?{query_string}')


@login_required
def delete_comment(request, comment_id):
    """
    A view to handle the deletion of comments
    that are associated with a specific blog post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    blog_post = comment.blog_post
    comment_owner = comment.author.user

    if not request.user == comment_owner:
        messages.error(request, 'Only the comment owner can delete comments.')
        return redirect(reverse('blog_post_detail', args=[blog_post.id]))

    comment.delete()

    messages.success(request, "Your comment has been deleted.")
    return redirect(reverse('blog_post_detail', args=[blog_post.id]))


@login_required
def comment_upvote(request, comment_id):
    """
    View to toggle helpful votes on a comment. If the
    user has already voted, the vote is removed. If the
    user hasn't voted, the vote is added.
    """
    comment = Comment.objects.get(id=comment_id)
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You must be logged in to upvote.")
        return redirect('blog_post_detail', comment.blog_post.id)

    if user in comment.comment_upvotes.all():
        comment.comment_upvotes.remove(user)
        messages.success(request, "You have removed your upvote.")
    else:
        comment.comment_upvotes.add(user)
        messages.success(request, "You have added your upvote.")

    return redirect('blog_post_detail', comment.blog_post.id)


@login_required
def approve_comment(request, comment_id):
    """
    A view to approve comments that are associated with a specific blog post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if not request.user.is_superuser:
        messages.error(request, 'Only superusers can approve comments.')
        return redirect(reverse('home'))

    comment.is_approved = True
    comment.save()

    messages.success(request, "The comment has been approved.")
    return redirect(reverse('profile'))
