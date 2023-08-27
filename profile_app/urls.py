from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
     path('users_orders/<order_id>', views.users_orders, name='users_orders'),
    ]