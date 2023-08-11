from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from shopping_bag.context_processor import *
from .models import *
from .forms import *
from products.models import *
from django.views.decorators.http import require_POST
from django.conf import settings

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
                    
                except Product.DoesNotExist:
                    #error message

                    official_order.delete()
                    return redirect(reverse('shopping_bag_items'))
            return redirect(reverse('success_purchase', args=[official_order.order_id]))
        else:
            pass # issue with form
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            # message nothing in bag
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
                pass #profile details
            except:
                pass #UserProfile DoesNotExist
        else:
            form_checkout = OrderForm()

    if not stripe_public_key:
        pass #error message

    template = 'checkout/checkout_page.html'
    context = {
        'order_form': form_checkout,
        'client_secret': intent.client_secret,
        'stripe_public_key': stripe_public_key
    }

    return render(request, template, context)

def success_purchase(request, order_id):

    # if user wants to save info
    save_info = request.session.get('save_info')
    official_order = get_object_or_404(Order, order_id=order_id)

    if request.user.is_authenticated:
        #connect profile
        official_order.save()

        if save_info:
            pass # save the uinfo to profile

    # success message

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
        #error message
        return HttpResponse(content=e, status=400)