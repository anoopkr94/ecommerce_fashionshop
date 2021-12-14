from django.db import models

class order_details(models.Model):
    user=models.CharField(max_length=50)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    address=models.TextField()
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pin=models.IntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    gt=models.DecimalField(default=0.00,decimal_places=2,max_digits=10)
    date=models.DateField()

class order_items(models.Model):
    order_id=models.IntegerField()
    user=models.CharField(max_length=50)
    pro_id = models.IntegerField()
    name=models.CharField(max_length=50)
    image = models.ImageField()
    seller = models.CharField(max_length=20)
    qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    total=models.DecimalField(default=0.00,decimal_places=2,max_digits=10)
    status=models.CharField(max_length=200)

class payment(models.Model):
    order_id = models.IntegerField()
    user=models.CharField(max_length=50)
    type=models.CharField(max_length=10)
    card_no=models.CharField(max_length=50,null=True)
    card_name = models.CharField(max_length=50,null=True)
    month=models.IntegerField(null=True)
    year=models.IntegerField(null=True)
    cvv=models.IntegerField(null=True)
    amount=models.DecimalField(default=0.00,decimal_places=2,max_digits=10,null=True)
# Create your models here.
