from django.contrib import admin
from .models import order_items,payment,order_details

admin.site.register(order_items)
admin.site.register(payment)
admin.site.register(order_details)
# Register your models here.
