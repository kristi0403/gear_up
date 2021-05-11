from django.contrib import admin
from .models import Product, Category, Platform, Special_category, Sub_category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'platform',
        'special_category',
        'sub_category',
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


class Special_categoryAdmin(admin.ModelAdmin):
    list_display = {
        'friendly_name',
        'name',
    }


class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = {
        'friendly_name',
        'name',
    }


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Special_category)
admin.site.register(Sub_category)
