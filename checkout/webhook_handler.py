from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import stripe
import json
import time
from products.models import *
from .models import *


class Stripe_Webhook_Handler:
    """Handle Stripe webhook."""

    def __init__(self, request):
        """Initialize a new instance of Stripe Webhook handler class."""
        self.request = request

    def handle_event(self, event):
        """Handle a generic webhook event."""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the succssful payment intent events."""
        payment_intent = event.data.object
        pid = payment_intent.id
        shopping_bag = payment_intent.metadata.shopping_bag
        save_info = payment_intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            payment_intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = payment_intent.shipping
        overall_total = stripe_charge.amount / 100

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        user_profile = None
        username = payment_intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = WebsiteUser.objects.get(website_user__username=username)
            if save_info:
                user_profile.default_phone_number = shipping_details.phone
                user_profile.default_street_address1 = shipping_details.address.line1
                user_profile.default_street_address2 = shipping_details.address.line2
                user_profile.default_town_or_city = shipping_details.address.city
                user_profile.default_county = shipping_details.address.state
                user_profile.default_postcode = shipping_details.address.postal_code
                user_profile.default_country = shipping_details.address.country
                user_profile.save()

        order_exists = False
        creation_attempt = 1
        while creation_attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    final_total=overall_total,
                    original_shopping_bag=shopping_bag,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                creation_attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=(f'Webhook received - Order in system'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    profile_id=user_profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_shopping_bag=shopping_bag,
                    stripe_pid=pid,
                )
                for item_identity, data in json.loads(shopping_bag).items():
                    specific_product = Product.objects.get(id=item_identity)
                    if isinstance(data, int):
                        order_item = OrderItem(
                            product_id=specific_product,
                            order_id=order,
                            quantity=data,
                        )
                        order_item.save()
            except:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Error with Order. Try again Later.',
                    status=500)

        return HttpResponse(
            content=(f'Order created in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment_intent.payment_failed."""
        return HttpResponse(
            content=f'Payment Failed: {event["type"]}',
            status=200)
