from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.db.models import Q

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
                #error message
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