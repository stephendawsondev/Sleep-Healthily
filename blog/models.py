from django.db import models
from django.urls import reverse

from profiles.models import UserProfile

STATUS = ((0, 'Draft'), (1, 'Published'))


class BlogPost(models.Model):
    """
    Blog post model. Fields:
    - title
    - slug
    - content
    - excerpt
    - tags
    - category
    - created_on
    - updated_on
    - author
    - favourited
    - image
    - status
    """
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE, related_name='blog_posts'
    )
    featured_image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='blog_posts')
    category = models.ManyToManyField('Category', related_name='blog_posts')
    favourited = models.ManyToManyField(
        'profiles.UserProfile', related_name='favourited_posts', blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.id, self.slug])

    def get_update_url(self):
        return reverse('edit_blog_post', args=[self.id])

    def get_delete_url(self):
        return reverse('delete_blog_post', args=[self.id])


class Tag(models.Model):
    """
    Tag model with name and slug. Fields:
    - name
    - slug
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model with name and slug. Fields:
    - name
    - slug
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Comment model for comments on blog posts. Fields:
    - blog_post
    - author
    - content
    - created on
    - updated on
    - is_approved
    """
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        'profiles.UserProfile', on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author} on {self.blog_post}'
