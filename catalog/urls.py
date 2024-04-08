from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]

