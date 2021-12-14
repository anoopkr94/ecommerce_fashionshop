from django.contrib import admin
from django.urls import path
from sellers import views

urlpatterns = [
    path('seller_home', views.seller_home, name='seller_home'),
    path('seller_add', views.seller_add, name='seller_add'),
    path('seller_view', views.seller_view, name='seller_view'),
    path('delete_item', views.delete_item, name='delete_item'),
    path('add_category', views.add_category, name='add_category'),
    path('add_type', views.add_type, name='add_type'),
    path('seller_order', views.seller_order, name='seller_order'),
    path('order_status,<int:id>', views.order_status, name='order_status'),
    path('ajax/load-types/', views.load_types, name='ajax_load_types'),  # AJAX
]