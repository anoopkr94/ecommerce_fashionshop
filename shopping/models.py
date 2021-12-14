from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return(self.name)
class type(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return(self.name)

class products(models.Model):
    
    size_choice = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )


    brand_ch=(("abc","abc"),("Adidas","Adidas"),("Roadster","Roadster"),("United","United"),("Nike","Nike"),("GAP","GAP"),("Levis","Levis"),("Benetton","Benetton"),
              ("Tommy Hilfiger","Tommy Hilfiger"),("Puma","Puma"),("Wildcraft","Wildcraft"))

    category=models.ForeignKey(category, on_delete=models.SET_NULL, blank=True, null=True)
    type=models.ForeignKey(type, on_delete=models.SET_NULL, blank=True, null=True)
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=30,choices=brand_ch)
    discription=models.TextField()
    mrp=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    image=models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    size=models.BooleanField()

    size=models.CharField(max_length=30,choices=size_choice)
    stock = models.PositiveIntegerField()
    seller=models.CharField(max_length=20,default="seller")

class wishlists(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class feedback(models.Model):
    product= models.ForeignKey(products,on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    date= models.DateField()
    message=models.CharField(max_length=200)




# Create your models here.
