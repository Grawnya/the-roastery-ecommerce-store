from django.shortcuts import render, get_object_or_404, redirect
from products.models import *

def shopping_bag_items(request):
    """view all items in the shopping bag """

    return render(request, 'shopping_bag/shopping_bag.html')

def add_item(request, item_id):
    """ add item to shopping bag """
    
    shopping_bag_item = get_object_or_404(Product, pk=item_id)
    order_quantity = int(request.POST.get('order_quantity'))

    shopping_bag = request.session.get('shopping_bag', {})
   
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += order_quantity
        # updated amount from original value success message
    else:
        shopping_bag[item_id] = order_quantity
        # added to bag success message

    request.session['shopping_bag'] = shopping_bag
    return redirect('products')
