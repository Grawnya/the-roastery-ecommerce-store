from django.shortcuts import render, redirect, reverse
from .models import *
from django.db.models import Q

def all_products(request):
    
    products = Product.objects.all()
    sort = None
    direction = None
    search = None

    if request.GET:
        print(request.GET)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
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