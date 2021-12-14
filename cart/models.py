from django.db import models
class cartitem(models.Model):
    pro_id=models.IntegerField()
    user=models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    seller=models.CharField(max_length=20)
    qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    total=models.DecimalField(default=0.00,decimal_places=2,max_digits=10)
# Create your models here.
