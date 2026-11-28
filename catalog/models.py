from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    category_describe = models.CharField(max_length=150, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название продукта')
    product_describe = models.TextField(verbose_name='Описание продукта')
    product_picture = models.ImageField(verbose_name='Изображение продукта', upload_to='images/')  # или будет урл?
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.FloatField(verbose_name='Цена продукта')
    created_at = models.DateField(verbose_name='Дата создания продукта')
    updated_at = models.DateField(verbose_name='Дата изменения продукта')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name']


class Contact(models.Model):
    contact_name = models.CharField(max_length=150, verbose_name='Название контакта')
    country = models.CharField(max_length=50, verbose_name='Название страны')
    NNN = models.CharField(max_length=150, verbose_name='ИНН')  # пока не понятно что это значит
    address = models.CharField(max_length=150, verbose_name='Адрес')

    def __str__(self):
        return f'{self.contact_name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['contact_name']
