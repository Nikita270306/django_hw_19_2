from django.urls import path

from catalog.views import index, home, contact

urlpatterns = [
    path('', index),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
]
