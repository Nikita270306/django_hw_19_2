# Generated by Django 5.0.1 on 2024-01-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='картинка')),
                ('category', models.CharField(verbose_name='категория')),
                ('price_per_unit', models.IntegerField(verbose_name='цена за штуку')),
                ('created_at', models.DateField(verbose_name='дата создания')),
                ('updated_at', models.DateField(verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
    ]
