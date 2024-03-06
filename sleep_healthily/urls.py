from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('review/', include('review.urls')),
    path('blog/', include('blog.urls')),
    path('policies/privacy/', views.privacy_policy, name='privacy_policy'),
    path('policies/shipping/', views.shipping_policy, name='shipping_policy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'sleep_healthily.views.handler404'
handler500 = 'sleep_healthily.views.handler500'
