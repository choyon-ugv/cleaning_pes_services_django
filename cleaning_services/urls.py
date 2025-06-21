from django.urls import path
from .views import appointment_view, home_view, about_view, services_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('appointment/', appointment_view, name='appointment'),
]