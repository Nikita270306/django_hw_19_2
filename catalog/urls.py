from django.urls import path

from catalog.views import index, contact, product_detail

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contact, name='contact'),
    path('product/<int:pk>', product_detail, name='product_detail')

]

