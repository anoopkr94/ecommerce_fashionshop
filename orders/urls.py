from django.contrib import admin
from django.urls import path
from orders import views
app_name='orders'
urlpatterns = [
    path('myorders', views.myorders, name='myorders'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('checkout', views.checkout, name='checkout'),
    path('placeorder',views.placeorder, name="placeorder"),
    path('add_address',views.add_address, name="add_address"),
    path('cash_on_delivery/<slug>',views.cash_on_delivery, name="cash_on_delivery"),
    path('online_payment/<slug>',views.online_payment, name="online_payment"),
    path('payment_status',views.payment_status, name="payment_status"),
    ]