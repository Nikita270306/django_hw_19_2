from catalog.models import Product
from django.shortcuts import render, get_object_or_404


def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'catalog/home.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def contact(request):
    return render(request, 'catalog/contacts.html')
