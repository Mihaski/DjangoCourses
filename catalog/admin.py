from django.contrib import admin

# Register your models here.

from .models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_category', 'product_price')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')
