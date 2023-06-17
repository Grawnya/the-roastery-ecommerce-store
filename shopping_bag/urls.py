from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag_items, name='shopping_bag_items'),
    path('add_item/<item_id>/', views.add_item, name='add_item'),
    path('update_item/<item_id>/', views.update_item, name='update_item'),
    path('delete_item/<item_id>/', views.delete_item, name='delete_item'),
    ]