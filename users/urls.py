from django.urls import path
from . import views

urlpatterns= [
      #path()
      path('register/',views.register,name="register"),
      path('details/',views.customer_details,name="customer_details"),
      path('profile/',views.profile,name='profile'),

]