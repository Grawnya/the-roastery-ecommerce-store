from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from products.models import *
from django.contrib import messages


def shopping_bag_items(request):
    """View all items in the shopping bag."""
    return render(request, 'shopping_bag/shopping_bag.html')


def add_item(request, item_id):
    """Add item to shopping bag."""
    shopping_bag_item = get_object_or_404(Product, pk=item_id)
    order_quantity = int(request.POST.get('order_quantity'))

    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += order_quantity
        messages.success(request, 'Shopping bag has been updated.')
    else:
        shopping_bag[item_id] = order_quantity
        messages.success(request,
                         f"{shopping_bag_item.name} added to shopping bag")

    request.session['shopping_bag'] = shopping_bag
    return redirect('products')


def update_item(request, item_id):
    """Update the quantity of the product to a new amount."""
    shopping_bag_item = get_object_or_404(Product, pk=item_id)
    order_quantity = int(request.POST.get('order_quantity'))

    shopping_bag = request.session.get('shopping_bag', {})

    if order_quantity > 0:
        shopping_bag[item_id] = order_quantity
        messages.success(request, 'Shopping bag has been updated.')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, 'Shopping bag has been updated.')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('shopping_bag_items'))


def delete_item(request, item_id):
    """Delete the product from the shopping bag."""
    try:
        shopping_bag_item = get_object_or_404(Product, pk=item_id)
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)
        messages.success(request, 'Shopping bag has been updated.')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except:
        messages.error(request, 'An error occurred. Please try again later.')
        return HttpResponse(status=500)
