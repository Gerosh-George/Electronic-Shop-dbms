from django.urls import path
from . import views

urlpatterns= [
       path('cart/',views.shopping_cart,name='cart'),
       path('additem/<int:pid>/<str:type>',views.addToCart,name='addItem'),
       path('deleteitem/<int:pid>/',views.deleteCartItem,name='deleteItem'),
       path('updatecolor/',views.updateColor,name='updateColor'),
       path('placeorder/',views.finalPurchase,name='placeOrder'),
       path('order-summary/<int:oid>',views.orderSummary,name='orderSummary'),
       
]