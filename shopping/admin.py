from django.contrib import admin
from .models import products,wishlists,feedback,category,type

admin.site.register(products)
admin.site.register(type)
admin.site.register(category)
admin.site.register(wishlists)
admin.site.register(feedback)


# Register your models here.
