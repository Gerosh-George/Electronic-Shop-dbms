from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from orders.models import Cart


# Create your views here.

def laptops(request):
    items=[x.item.name for x in Cart.objects.all() ]
    
    context={
        "laptops": Product.objects.filter(product_type='laptop'),
        "addedItems": items
    }    
    #return HttpResponse('Laptop Page')
    return render(request,'laptops.html',context)

def homepage_view(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')

def mobiles(request):
    #return HttpResponse('Hello World')
    items=[x.item.name for x in Cart.objects.all() ]
    
    context={
        "mobiles": Product.objects.filter(product_type='Mobile'),
        "addedItems": items
    }
    return render(request,'mobiles.html',context)


