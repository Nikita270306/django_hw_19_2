from catalog.models import Product
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactDetailView(TemplateView):
    template_name = 'catalog/contacts.html'
