
from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    return render(request, 'catalog/contacts.html')
