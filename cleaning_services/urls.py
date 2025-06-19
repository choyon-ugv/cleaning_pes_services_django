from django.urls import path
from .views import home, about, services, subscribe, contact, blog, blog_single

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about-us'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
]