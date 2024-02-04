from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_checkout, name='view_checkout'),
    path('order_summary/<order_number>',
         views.order_summary,
         name='order_summary'),
    path('cache_checkout_data/',
         views.cache_checkout_data,
         name='cache_checkout_data'),

]
