from django.contrib import admin
from .models import FinalOrder,Cart,UserOrderQuantity

# Register your models here.



class FinalOrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','date_ordered']

class CartAdmin(admin.ModelAdmin):
    list_display=['item']

class UserOrderQuantityAdmin(admin.ModelAdmin):
    list_display=['order','product','color']

    
admin.site.register(FinalOrder,FinalOrderAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(UserOrderQuantity,UserOrderQuantityAdmin)