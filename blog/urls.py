from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('<int:id>/', views.blog_post_detail, name='blog_post_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<int:id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<int:blog_post_id>/',
         views.delete_blog_post, name='delete_blog_post'),
    path('favourite_blog_post/<int:blog_post_id>/', views.favourite_blog_post,
         name='favourite_blog_post'),
    path('<int:blog_post_id>/comment/add/',
         views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('comment_upvote/<int:comment_id>/',
         views.comment_upvote, name='comment_upvote'),
    path('approve_comment/<int:comment_id>/',
         views.approve_comment, name='approve_comment'),
]
