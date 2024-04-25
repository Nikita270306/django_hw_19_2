from django.forms import inlineformset_factory
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        active_versions = {}

        for product in products:
            active_version = product.version_set.filter(current_version=True).first()
            if active_version is None:
                active_versions[product.pk] = None
            else:
                active_versions[product.pk] = active_version

        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        active_versions = {}

        for product in products:
            active_version = product.version_set.filter(current_version=True).first()
            if active_version is None:
                active_versions[product.pk] = None
            else:
                active_versions[product.pk] = active_version

        context['active_versions'] = active_versions
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_banned = any(word in form.cleaned_data['name'].lower() or
                                      word in form.cleaned_data['description'].lower()
                                      for word in ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                                                   'free', 'scam', 'police', 'radar'])
        form.instance.last_modified_date = timezone.now()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'catalog/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        active_versions = {}

        for product in products:
            active_version = product.version_set.filter(current_version=True).first()
            if active_version is None:
                active_versions[product.pk] = None
            else:
                active_versions[product.pk] = active_version

        context['active_versions'] = active_versions
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self):
        return reverse_lazy('catalog:product-detail', kwargs={'pk': self.object.pk})


class ContactDetailView(TemplateView):
    template_name = 'catalog/contacts.html'


class VersionDetailView(DetailView):
    model = Version
    template_name = 'catalog/version_detail.html'
    context_object_name = 'version'

    def get_object(self, queryset=None):
        version_id = self.kwargs.get('version_id')
        return Version.objects.get(id=version_id)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionCreateForm
    template_name = 'catalog/version_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:home')


class VersionUpdateView(UpdateView):
    model = Version
    template_name = 'catalog/version_form.html'
    form_class = VersionUpdateForm

    def get_success_url(self):
        return reverse('catalog:version-detail', kwargs={'version_id': self.object.pk})
