from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    """Product admin table."""

    list_display = (
        'sku',
        'name',
        'roast',
        'location',
        'origin',
        'bag_100g_USD',
        'rating',
        'review',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
