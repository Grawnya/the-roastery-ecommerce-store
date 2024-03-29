from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

from checkout.models import Order


@login_required
def profile(request):
    """Create/update a profile."""
    profile = get_object_or_404(WebsiteUser, website_user=request.user)

    if request.method == 'POST':
        profile_form = WebsiteUserForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.error(request, 'Profile details have been saved.')
        else:
            messages.error(request, 'An error occurred.'
                           ' Please try again later.')

        favourites_form = FavouritesForm(request.POST, instance=profile)
        if favourites_form.is_valid():
            favourites_form.save()
        else:
            messages.error(request, 'An error occurred.'
                           ' Please try again later.')
    else:
        profile_form = WebsiteUserForm(instance=profile)
        favourites_form = FavouritesForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile_app/profile.html'
    context = {
        'profile_form': profile_form,
        'favourites_form': favourites_form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def users_orders(request, order_id):
    """See user's orders on profile page."""
    order = get_object_or_404(Order, order_id=order_id)

    template = 'checkout/success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
