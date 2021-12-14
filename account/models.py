from django.db import models
class user_details(models.Model):
    user=models.CharField(max_length=50)
    type=models.CharField(max_length=10)

# Create your models here.
