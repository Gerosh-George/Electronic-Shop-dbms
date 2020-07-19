from django.db import models

# Create your models here.


class Product(models.Model):
    product_type=models.CharField(max_length=10)
    name=models.CharField(max_length=240)
    price=models.FloatField()
    stock=models.PositiveIntegerField()
    image_url=models.CharField(max_length=2083)

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.CharField(max_length=10)

    def __str__(self):
        return self.color
    
