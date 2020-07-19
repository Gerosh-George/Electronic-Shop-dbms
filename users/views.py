from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, CustomerDetailsForm
from orders.models import FinalOrder
from .models import Customer
from django.contrib.auth import login


# Create your views here.

def register(request):
    # form= UserCreationForm()
    # return render(request,'register.html',{'form':form})
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save()


            login(request, instance)
            return redirect('customer_details')

    else:
        form=UserRegisterForm()
    return render(request,'registration.html', {'form':form})


def customer_details(request):
    if request.method=="POST":
        form=CustomerDetailsForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
           
            instance.user=request.user
            instance.email=request.user.email
            instance.save()
            return redirect('home')
    else:
        form=CustomerDetailsForm()
    return render(request,'details.html',{'form':form})


def profile(request):
    customer=Customer.objects.filter(user=request.user)[0]
    previous_orders=FinalOrder.objects.filter(customer=customer)

    context={
        'previous_orders':previous_orders,
    }

    return render(request,'profile.html',context)




