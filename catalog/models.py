from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название продукта')
    product_describe = models.CharField(max_length=150, verbose_name='Описание продукта')
    product_picture = models.ImageField(verbose_name='Изображение продукта', upload_to='images/')  # или будет урл?
    product_category = models.CharField(max_length=150, verbose_name='Категория продукта')
    product_price = models.FloatField(verbose_name='Цена продукта')
    created_at = models.DateField(verbose_name='Дата создания продукта')
    updated_at = models.DateField(verbose_name='Дата изменения продукта')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name']


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    category_describe = models.CharField(max_length=150, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']
