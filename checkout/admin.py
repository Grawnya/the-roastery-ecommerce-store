from django.contrib import admin
from .models import *

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total_price',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_id', 'order_date', 'items_total',
                       'final_total', 'original_shopping_bag',
                       'stripe_pid')

    fields = ('order_id', 'order_date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 
              'postcode', 'country', 'items_total', 'delivery_cost', 
              'final_total', 'original_shopping_bag', 'stripe_pid')

    list_display = ('order_id', 'order_date', 'full_name',
                    'items_total', 'delivery_cost',
                    'final_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)