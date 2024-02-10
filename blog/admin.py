from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost, Tag, Category, Comment


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """
    Displays Admin controls for blog posts.
    """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'content']

    summernote_fields = 'content, excerpt'


class TagAdmin(admin.ModelAdmin):
    """
    Displays Admin controls for tags.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    """
    Displays Admin controls for categories.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


class CommentAdmin(admin.ModelAdmin):
    """
    Displays Admin controls for comments.
    """
    list_display = ('blog_post', 'author', 'created_on', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('author', 'content')

    def approve_comments(self, request, queryset):
        """
        Approves comments in bulk.
        """
        queryset.update(is_approved=True)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
