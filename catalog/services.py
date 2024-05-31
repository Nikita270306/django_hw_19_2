from django.conf import settings
from django.core.cache import cache

from catalog.models import Category
from user.models import CustomUser


def get_cached_categories():
    categories = cache.get('categories')
    if not categories:
        if settings.СACHE_ENABLED:
            key = 'category_list'
            categories = cache.get(key)
            if not categories:
                categories = list(Category.objects.all())
                cache.set(key, categories, 60 * 60)
        else:
            categories = list(Category.objects.all())
            cache.set('categories', categories, 60 * 60)
    return categories


def get_cached_customers_for_dish(product_pk):
    if settings.СACHE_ENABLED:
        key = f"customer_list{product_pk}"
        user_list = cache.get(key)
        if user_list is None:
            user_list = CustomUser.objects.filter(product_pk=product_pk)
            cache.set(key, user_list)
    else:
        user_list = CustomUser.objects.filter(product_pk=product_pk)

    return user_list
