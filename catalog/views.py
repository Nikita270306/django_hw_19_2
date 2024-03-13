from catalog.models import Product
from django.shortcuts import render


def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'catalog/home.html', context)


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    return render(request, 'catalog/contacts.html')
