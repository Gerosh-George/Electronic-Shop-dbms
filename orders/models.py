from django.db import models
from products.models import Product,ProductColor
from users.models import Customer
# Create your models here.


class Cart(models.Model):
    item=models.OneToOneField(Product,on_delete=models.SET_NULL,null=True)
    color=models.ForeignKey(ProductColor,on_delete=models.SET_NULL,null=True)    

    def __str__(self):
        return f"{self.item}"

    


class FinalOrder(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE ,null=True)
    date_ordered=models.DateField(auto_now=True)
    total=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.customer} "+ f"{self.id}"
    
    def cart_total():
        total=0
        for product in Cart.objects.all():
            total=total+product.item.price
        return total 

class UserOrderQuantity(models.Model):
    order=models.ForeignKey(FinalOrder,on_delete=models.CASCADE,default=None)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    color=models.ForeignKey(ProductColor,on_delete=models.SET_NULL,null=True) 

    def __str__(self):
        return f"{self.product}"+" "+f"{self.color}"   
