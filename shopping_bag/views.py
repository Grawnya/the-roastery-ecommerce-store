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

def update_bag(request, item_id):
    """Update the quantity of the product to a new amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))