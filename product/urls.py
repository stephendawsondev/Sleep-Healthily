from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
]
