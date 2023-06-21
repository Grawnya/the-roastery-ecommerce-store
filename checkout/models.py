from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import *

import uuid
from django_countries.fields import CountryField




class Order(models.Model):
    order_id = models.CharField(max_length=24, null=False, editable=False)
    # profile_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    items_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    final_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_shopping_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _order_id_creation(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        pass

    def save_order(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self._order_id_creation()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id