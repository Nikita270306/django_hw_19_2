import json
from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        products_list = []
        with open('catalog/fixtures/product.json', encoding='utf-8') as f:
            dict_prod = json.load(f)

        for product in dict_prod:
            products_list.append(Product(name=product['fields']['name'], description=product['fields']['description']))

        Product.objects.bulk_create(products_list)

