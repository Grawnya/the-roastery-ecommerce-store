from django.shortcuts import render 

def index(request):
    '''
    A view to return the index page
    '''
    return render(request, 'home/index.html')

def error_404(request, exception):
    '''404 page'''
    return render(request, '404.html')

def error_500(request):
    '''500 page'''
    return render(request, '500.html', data)