from django.shortcuts import render


def index(request):
    """View to return the index page."""
    return render(request, 'home/index.html')


def error_404(request, exception):
    """Show 404 page."""
    return render(request, '404.html')


def error_500(request):
    """Show 500 page."""
    context = {
        'error_message': 'An internal server error occurred.',
    }
    return render(request, '500.html', context)
