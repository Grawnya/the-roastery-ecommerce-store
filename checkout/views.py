from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from shopping_bag.context_processor import *
from .models import *
from .forms import *
from products.models import *
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

import stripe
import json

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        checkout_form = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country']
        }

        form_checkout = OrderForm(checkout_form)

        if form_checkout.is_valid():

            official_order = form_checkout.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            official_order.original_shopping_bag = json.dumps(shopping_bag)
            official_order.save()
            
            for item_identity, data in shopping_bag.items():
                try:
                    specific_product = Product.objects.get(id=item_identity)
                    if isinstance(data, int):
                        order_item = OrderItem(
                            product_id=specific_product,
                            order_id=official_order,
                            quantity=data,
                        )
                        order_item.save()
                        official_order.final_total += specific_product.bag_100g_USD * data
                    

                except Product.DoesNotExist:
                    messages.error(request, 'Product does not exist.')

                    official_order.delete()
                    return redirect(reverse('shopping_bag_items'))
            
            official_order.final_total += settings.WORLDWIDE_DELIVERY_COST
            official_order.save()

            return redirect(reverse('success_purchase', args=[official_order.order_id]))
        else:
            messages.error(request, 'An error occurred with the form. Please try again later.')
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            messages.error(request, 'Nothing is in the shopping bag.')
            return redirect(reverse('products'))

        active_bag = current_shopping_bag_content(request)
        final_total = active_bag['final_value']
        stripe.api_key = stripe_secret_key
        stripe_overall_total = round(final_total * 100)
        intent = stripe.PaymentIntent.create(
            amount=stripe_overall_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        if request.user.is_authenticated:
            try:
                profile = WebsiteUser.objects.get(website_user=request.user)
                form_checkout = OrderForm(initial={
                    'full_name': profile.profile_full_name,
                    'email': profile.profile_email,
                    'phone_number': profile.profile_phone_number,
                    'street_address1': profile.profile_street_address1,
                    'street_address2': profile.profile_street_address2,
                    'town_or_city': profile.profile_town_or_city,
                    'county': profile.profile_county,
                    'postcode': profile.profile_postcode,
                    'country': profile.profile_country,
                })
            except WebsiteUser.DoesNotExist:
                form_checkout = OrderForm()
        else:
            form_checkout = OrderForm()

    if not stripe_public_key:
        messages.error(request, 'An error occurred with the stripe public key. Please contact the page admin.')

    template = 'checkout/checkout_page.html'
    context = {
        'order_form': form_checkout,
        'client_secret': intent.client_secret,
        'stripe_public_key': stripe_public_key
    }

    return render(request, template, context)

def success_purchase(request, order_id):

    save_info = request.session.get('save_info')
    official_order = get_object_or_404(Order, order_id=order_id)

    if request.user.is_authenticated:
        profile = WebsiteUser.objects.get(website_user=request.user)
        official_order.profile_id = profile
        official_order.save()
        if save_info:
            profile_data = {
                'profile_phone_number': official_order.phone_number,
                'profile_street_address1': official_order.street_address1,
                'profile_street_address2': official_order.street_address2,
                'profile_town_or_city': official_order.town_or_city,
                'profile_county': official_order.county,
                'profile_postcode': official_order.postcode,
                'profile_country': official_order.country,
            }

            website_user_form = WebsiteUserForm(profile_data, instance=profile)
            if website_user_form.is_valid():
                website_user_form.save()

    messages.success(request, 'Successful purchase!.')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'checkout/success.html'
    context = {
        'order': official_order,
    }
        
    return render(request, template, context)

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shopping_bag': json.dumps(request.session.get('shopping_bag', {})),
            'username': request.user,
            'save_info': request.POST.get('save_info'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, e)
        return HttpResponse(content=e, status=400)