from django import forms
from .models import *


class WebsiteUserForm(forms.ModelForm):
    """Form for the WebsiteUser model."""

    class Meta:
        """Format of the WebsiteUserForm."""

        model = WebsiteUser
        exclude = ('website_user',)

    def __init__(self, *args, **kwargs):
        """Create instance of WebsiteUserForm."""
        super().__init__(*args, **kwargs)
        placeholders = {
            'profile_full_name': 'Full Name',
            'profile_email': 'Email',
            'profile_phone_number': 'Phone Number',
            'profile_town_or_city': 'Town or City',
            'profile_street_address1': 'Street Address 1',
            'profile_street_address2': 'Street Address 2',
            'profile_county': 'County, State or Locality',
            'profile_postcode': 'Postcode',
            'profile_country': 'Country',
        }

        self.fields['profile_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'profile_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class FavouritesForm(forms.ModelForm):
    """Form for the Favourites model."""

    class Meta:
        """Format of the FavouriteForm."""

        model = Favourites
        fields = ('birthday', 'coffee_type', 'roast')
        labels = {
            'birthday': 'Birthday',
            'coffee_type': 'Coffee Location',
            'roast': 'Roast Type'
        }
        widgets = {
                   'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
