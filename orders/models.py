from django.db import models
from django.conf import settings
from shopping.models import products

# Create your models here.
class address(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address1=models.TextField()
    address2=models.TextField(null=True)
    zipcode=models.PositiveIntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.PositiveIntegerField()



class order(models.Model):
    status=(('Process',"Process"),('Payment Success',"Payment Success"),('Shipped',"Shipped"),
            ('Deliverd',"Deliverd"),("order cancelled","order cancelled"),("return acepted","return acepted"),("refunded","refunded"))
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    address=models.ForeignKey(address,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=30,choices=status,default="Process")


class order_item(models.Model):
    orders=models.ForeignKey(order,on_delete=models.CASCADE)
    item=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def get_total_item_price(self):
        return self.quantity * self.item.price


class payment(models.Model):
    orders=models.ForeignKey(order,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)