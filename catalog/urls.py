from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import ProductListView, ProductDetailView, ContactDetailView, ProductUpdateView, ProductCreateView, \
    VersionDetailView, VersionCreateView, VersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', cache_page(60)(ContactDetailView.as_view()), name='contact'),
    path('product/<int:pk>', never_cache(ProductDetailView.as_view()), name='product_detail'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='update_product'),

    path('version/<int:version_id>/', VersionDetailView.as_view(), name='version-detail'),
    path('version/form/<int:pk>/', never_cache(VersionCreateView.as_view()), name='version-form'),
    path('version/edit/<int:pk>/', never_cache(VersionUpdateView.as_view()), name='version-edit'),

]

