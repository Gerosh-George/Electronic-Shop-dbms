from django.urls import path
from . import views



urlpatterns = [
    path('mobiles/',views.mobiles,name='mobiles'),
    path('laptops/',views.laptops,name='laptops'),
   
]

