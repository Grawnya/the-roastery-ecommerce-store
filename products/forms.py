from django import forms
from .widgets import CustomClearableFileInput
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('sku', 'name', 'roast', 'location', 'origin',
                  'bag_100g_USD', 'rating', 'review', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'sku': 'Stock Keeping Unit (sku) Number',
            'name': 'Product Name',
            'roast': 'Roast Type',
            'location': 'Continent',
            'origin': 'Country',
            'bag_100g_USD': 'Price per 100g Bag',
            'rating': 'Rating out of 100',
            'review': 'Review',
            'image': 'Image',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False