from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart,FinalOrder,UserOrderQuantity
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from products.models import Product,ProductColor
from users.models import Customer
# Create your views here.


def shopping_cart(request):
    total=FinalOrder.cart_total()
    context={
        "items":Cart.objects.all(),
        "total":total,
        'colors':ProductColor.objects.all(),
    }
    return render(request, 'cart.html',context)


def addToCart(request, pid, type):
    product = Product.objects.filter(pk=pid).first()
    flag = True
    for cart in Cart.objects.all():
        if(product.name == cart.item.name):
            flag = False
            break
    
    if(flag == True):
        color=ProductColor.objects.filter(product=product).first()
        addedItem = Cart(
            item=product,
            color=color
        )
        addedItem.save()
    else:
        messages.info(request,"This item is already added to the cart")
       

    if(type == 'mobile'):
        return redirect(reverse('mobiles',))

    else:
        return redirect(reverse('laptops'))

def deleteCartItem(request, pid):
    product_to_delete = Cart.objects.filter(pk=pid)
    if product_to_delete.exists():
        product_to_delete[0].delete()
    return redirect(reverse('cart'))

def updateColor(request):
    message=''
    if request.method=='POST':
        product=request.POST['title']
        
        cartItem=Cart()
        for cart in Cart.objects.all():
            if(cart.item.name==product):
                cartItem=cart
                break
        cartItem.color=ProductColor.objects.filter(product=cart.item,color=request.POST['color']).first()
        cartItem.save()
        message='update successful'
    return HttpResponse(message)


@login_required
def finalPurchase(request):
    order=FinalOrder()

    user=request.user
    cur_customer=Customer.objects.filter(user=user).first()
    order.customer=cur_customer
    order.total=FinalOrder.cart_total()
    order.save()

      
    userOrderedProductManager(request,order) 

    return redirect('orderSummary',order.id )
        
def userOrderedProductManager(request,order):
    for cart in Cart.objects.all():
        manager=UserOrderQuantity()
        manager.order=order
        manager.product=cart.item
        manager.product.stock=manager.product.stock - 1
        manager.product.save()
        manager.color=cart.color
        manager.save()
    Cart.objects.all().delete()
    messages.success(request,'Order has been placed successfully')
    return


def orderSummary(request, oid):
    #customer_order=FinalOrder.objects.last()
    customer_order=FinalOrder.objects.filter(pk=oid)[0]
    product_ordered=UserOrderQuantity.objects.filter(order=customer_order)
    context={
        "order_details":customer_order,
        "product_details":product_ordered,

    }
    return render(request,'order_summary.html',context)
