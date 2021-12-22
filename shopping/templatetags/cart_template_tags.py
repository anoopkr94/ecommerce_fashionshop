from urllib import request
from django import template
from django.utils.safestring import mark_safe
from cart.models import cartitems
from shopping.models import category, type

register = template.Library()



@register.filter
def cart_item_counts(user):
    items = cartitems.objects.filter(user=user)
    count = 0
    for i in items:
        count+=i.quantity
    return mark_safe(count)


@register.simple_tag
def categories():
    items = category.objects.all()
    items_li = ""
    for i in items:
        items_li += """<li><a href="../products/{}">{}</a></li>""".format(i.name, i.name)
    return mark_safe(items_li)


@register.simple_tag
def types_list():
    cats=category.objects.all()
    types = type.objects.all()
    items_li = ""
    for c in cats:
        items_li += """<div class="col-lg">
                                   <h1 class="dropdown-header"><a href="../products/{}">{}</a></h1>""".format(c.name, c.name)

        for i in types:
            cat = c.name

            if cat == i.category.name:

                items_li += """<li><a href="../type_shop,{}">{}</a></li>""".format(i.name, i.name)

            cat=i.category.name
        items_li +="""</div>"""
    return mark_safe(items_li)
