from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.specific_product, name='specific_product'),
    path('new_product/', views.create_new_product, name='new_product'),
    ]