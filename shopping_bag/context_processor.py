from django.shortcuts import get_object_or_404
from products.models import Product


def current_shopping_bag_content(request):
    """ shopping bag contents in the current open session """

    items_in_shopping_bag = []
    final_value = 0
    item_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        final_value += quantity * product.bag_100g_USD
        item_count += quantity
        
        items_in_shopping_bag.append({'item_id': item_id,
                                      'quantity': quantity,
                                      'product': product})

    context = {
        'items_in_shopping_bag': items_in_shopping_bag,
        'final_value': final_value,
        'item_count': item_count,
        'shopping_bag': shopping_bag,
    }

    return context