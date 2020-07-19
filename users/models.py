from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=240)     
    address=models.CharField(max_length=64,default=None)
    phone_number=PhoneField(help_text='Contact number',default=None) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    
    
    def __str__(self):
        return self.name
  
    



    
