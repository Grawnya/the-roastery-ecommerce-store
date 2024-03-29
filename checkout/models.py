from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import *
from profile_app.models import *

import uuid
from django_countries.fields import CountryField


class Order(models.Model):
    """Order Model to save an order."""

    order_id = models.CharField(max_length=300, null=False, editable=False)
    profile_id = models.ForeignKey(WebsiteUser, on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='orders')
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False,
                                       blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    items_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    final_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_shopping_bag = models.TextField(null=False, blank=False,
                                             default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _order_id_creation(self):
        """Create order ID."""
        return uuid.uuid4().hex.upper()

    def set_delivery_cost(self):
        """Set the delivery cost."""
        self.delivery_cost = settings.WORLDWIDE_DELIVERY_COST
        self.save()

    def update_total(self):
        """Update final total."""
        self.final_total = self.items_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """Save the order."""
        if not self.order_id:
            self.order_id = self._order_id_creation()
        super().save(*args, **kwargs)

    def __str__(self):
        """Representation of Order Model."""
        return self.order_id


class OrderItem(models.Model):
    """Model to focus on specific item in the order."""

    product_id = models.ForeignKey(Product, null=False, blank=False,
                                   on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='items')
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total_price = models.DecimalField(max_digits=6, decimal_places=2,
                                           null=False, blank=False,
                                           editable=False)

    def save(self, *args, **kwargs):
        """Save the Order Item."""
        self.item_total_price = self.product_id.bag_100g_USD * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """Representation of Order Item."""
        return f'SKU: {self.product_id.sku} for {self.product_id.name}'
