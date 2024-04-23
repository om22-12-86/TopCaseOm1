# carts_tags.py
from django import template
from carts.models import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def user_carts(context):
    request = context['request']
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    return Cart.objects.filter(user_id=user_id)
