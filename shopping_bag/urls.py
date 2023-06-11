from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag_items, name='shopping_bag_items'),
    path('add_item/<item_id>', views.add_item, name='add_item'),
    ]