from django.urls import path

from catalog.views import index, home, contact

urlpatterns = [
    path('', index),
    path('home/', home, name='home'),
    path('contacts/', contact, name='contact'),
]
