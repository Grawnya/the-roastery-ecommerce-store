from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    """Order Form."""

    class Meta:
        """Meta Details of the Order Form."""

        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of OrderForm."""
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Post Code',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
