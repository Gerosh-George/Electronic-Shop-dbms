from django.contrib import admin
from .models import Product,ProductColor

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock']

class ProductColorAdmin(admin.ModelAdmin):
    list_display=['product','color']


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductColor,ProductColorAdmin)

