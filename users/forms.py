from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class UserRegisterForm(UserCreationForm):
    email=forms.CharField()

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','address']


