from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='картинка', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price_per_unit = models.IntegerField(verbose_name='цена за штуку')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price_per_unit}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
