from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def all_products(request):
    
    products = Product.objects.all()
    sort = None
    direction = None
    search = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'descending':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'search_bar' in request.GET:
            search = request.GET['search_bar']
            if 'roast' in search:
                search = search.replace('roast', '')
            if not search:
                messages.error(request, 'An error with the search bar. Please try again later.')
                return redirect(reverse('products'))

            queries = Q(name__icontains=search) | Q(review__icontains=search) | Q(roast__icontains=search)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'filter_element': current_sorting,
    }

    return render(request, 'products/products.html', context)


def specific_product(request, product_id):

    specific_product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': specific_product,
    }

    return render(request, 'products/specific_product.html', context)


@login_required
def create_new_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        new_product_form = ProductForm(request.POST, request.FILES)

        if new_product_form.is_valid():
            new_product = new_product_form.save()
            messages.success(request, 'New product added.')
            return redirect(reverse('specific_product', args=[new_product.id]))
        else:
            messages.error(request, 'An error occurred. Please try again later.')
    else:
        new_product_form = ProductForm()

    template = 'products/new_product.html'
    
    context = {
        'form': new_product_form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('home'))

    specific_product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=specific_product)
        
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Product has been successfully updated.')
            return redirect(reverse('specific_product', args=[specific_product.id]))
        else:
           messages.error(request, 'An error occurred. Please try again later.')
    else:
        product_form = ProductForm(instance=specific_product)

    template = 'products/edit_product.html'
    context = {
        'form': product_form,
        'product': specific_product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'An error occurred. Please try again later.')
        return redirect(reverse('home'))

    specific_product = get_object_or_404(Product, pk=product_id)
    specific_product.delete()
    messages.success(request, 'Product has been deleted.')
    return redirect(reverse('products'))