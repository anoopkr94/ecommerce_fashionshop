from django.contrib import admin
from .models import payment,address,order,order_item

admin.site.register(address)
admin.site.register(payment)
admin.site.register(order_item)
admin.site.register(order)
# Register your models here.
