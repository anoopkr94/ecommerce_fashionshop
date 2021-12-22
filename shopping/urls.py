"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopping import views
app_name='shopping'
urlpatterns = [
    path('',views.index,name='index'),
    path('home', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
    path('product,<int:id>', views.product, name='product'),
    path('products/<str:name>', views.product_s, name='products'),
    path('type_shop,<str:name>', views.type_shop, name='type_shop'),
    path('wishlist,<int:id>',views.wishlist,name='wishlist'),
    path('search', views.search, name='search'),
    path('wishlist_view', views.wishlist_view, name='wishlist_view'),
    path('delete_wishlist,<int:id>', views.delete_wishlist, name='delete_wishlist'),
    path('feedback', views.feed, name='feedback'),


]
