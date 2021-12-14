from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path('myorders', views.myorders, name='myorders'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('payments', views.payments, name='payments'),
    path('checkout', views.checkout, name='checkout'),
    ]