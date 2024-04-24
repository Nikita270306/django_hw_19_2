from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from catalog.forms import ProductCreateForm, ProductUpdateForm, VersionCreateForm, VersionUpdateForm
from catalog.models import Product, Version
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_banned = any(word in form.cleaned_data['name'].lower() or
                                      word in form.cleaned_data['description'].lower()
                                      for word in ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                                                   'free', 'scam', 'police', 'radar'])
        form.instance.last_modified_date = timezone.now()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    class ProductUpdateView(UpdateView):
        model = Product
        form_class = ProductUpdateForm
        template_name = 'product/product_form.html'

        def get_object(self, queryset=None):
            self.object = super().get_object(queryset)
            if self.object.owner != self.request.user and not self.request.user.is_staff:
                raise Http404
            return self.object

        def get_success_url(self):
            return reverse_lazy('main_app:product-detail', kwargs={'pk': self.object.pk})

        def test_func(self):
            product = self.get_object()
            return self.request.user == product.owner


class ContactDetailView(TemplateView):
    template_name = 'catalog/contacts.html'


class VersionDetailView(DetailView):
    model = Version
    template_name = 'version/version_detail.html'
    context_object_name = 'version'

    def get_object(self, queryset=None):
        version_id = self.kwargs.get('version_id')
        return Version.objects.get(id=version_id)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionCreateForm
    template_name = 'version/version_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main_app:product-list')


class VersionUpdateView(UpdateView):
    model = Version
    template_name = 'version/version_form.html'
    form_class = VersionUpdateForm

    def get_success_url(self):
        return reverse('main:version-detail', kwargs={'version_id': self.object.pk})