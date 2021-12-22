from django.db import models
from django.conf import settings
from shopping.models import products

class cartitems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_total_item_price(self):
        return self.quantity * self.item.price
