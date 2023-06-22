from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(default=0,max_digits=100,decimal_places=2)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.productname
    

