from django.shortcuts import render
from shopping_bag.context_processor import *
from .models import *
from .forms import *

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

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

            for item_identify, data in shopping_bag.items():
                try:
                    specific_product = Product.objects.get(id=item_identify)
                    if isinstance(data, int):
                        order_item = OrderItem(
                            order=official_order,
                            product=specific_product,
                            quantity=data,
                        )
                        order_line_item.save()
                    
                except Product.DoesNotExist:
                    #error message

                    official_order.delete()
                    return redirect(reverse('shopping_bag_items'))

            # return redirect(reverse('checkout_success', args=[official_order.order_number]))
        else:
            pass # issue with form
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            # message nothing in bag
            return redirect(reverse('products'))

        active_bag = current_shopping_bag_content(request)
        final_total = active_bag['final_value']
        stripe_overall_total = round(final_total * 100)
        
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
        # payment intent client secret 'client_secret': intent.client_secret,
        'stripe_public_key': stripe_public_key
    }

    return render(request, template, context)