from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<order_no>', views.success_purchase, name='success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    ]

    