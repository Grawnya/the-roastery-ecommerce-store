from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings

def current_shopping_bag_content(request):
    """ shopping bag contents in the current open session """

    items_in_shopping_bag = []
    final_value = 0
    final_value_without_delivery = 0
    delivery_cost = settings.WORLDWIDE_DELIVERY_COST
    item_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        final_value_without_delivery += quantity * product.bag_100g_USD
        final_value = final_value_without_delivery + delivery_cost  
        item_count += quantity
        
        items_in_shopping_bag.append({'item_id': item_id,
                                      'quantity': quantity,
                                      'product': product})

    context = {
        'items_in_shopping_bag': items_in_shopping_bag,
        'final_value': final_value,
        'item_count': item_count,
        'shopping_bag': shopping_bag,
        'delivery_cost': delivery_cost
    }

    return context