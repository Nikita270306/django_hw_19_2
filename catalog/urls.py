from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactDetailView, ProductUpdateView, ProductCreateView, \
    VersionDetailView, VersionCreateView, VersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contact'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),

    path('version/<int:version_id>/', VersionDetailView.as_view(), name='version-detail'),
    path('version/form/<int:pk>/', VersionCreateView.as_view(), name='version-form'),
    path('version/edit/<int:pk>/', VersionUpdateView.as_view(), name='version-edit'),

]

