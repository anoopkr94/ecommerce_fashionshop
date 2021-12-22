from django.contrib import admin
from django.urls import path
from cart import views
app_name='cart'
urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('delete_cart/<int:id>', views.deletecartitem, name='delete_cart'),
    path('delete_qty_cart/<int:id>', views.remove_cartitem_qty, name='delete_qty_cart'),
    ]