from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('delete_cart,<int:id>', views.delete_cart, name='delete_cart'),
    path('delete_qty_cart,<int:id>', views.delete_qty_cart, name='delete_qty_cart'),
    ]