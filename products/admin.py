from django.contrib import admin
from .models import Product, Category, Platform

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'platform'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = {
        'friendly_name',
        'name',
    }


class PlatformAdmin(admin.ModelAdmin):
    list_display = {
        'friendly_name',
        'name',
    }


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Platform)
