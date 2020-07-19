from django import template
from orders.models import Cart
from users.models import Customer

register = template.Library() 

@register.simple_tag
def cart_item_count():
    return Cart.objects.all().count()

@register.simple_tag
def profile(user):
    customer=Customer.objects.filter(user=user)[0]
    return customer.name

