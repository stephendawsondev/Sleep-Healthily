from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.create_review, name='create_review'),
    path('helpful_votes/<int:review_id>/',
         views.helpful_votes, name='helpful_votes'),
]
