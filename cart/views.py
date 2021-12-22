from django.shortcuts import get_object_or_404, render,redirect
from .models import cartitems
from shopping.models import products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='shopping:login')
def addtocart(request,id):
    product = get_object_or_404(products, id=id)
    orderitem, created = cartitems.objects.get_or_create(item=product,user=request.user)

    if cartitems.objects.filter(item__id=id, user=request.user).exists():
        orderitem.quantity +=1
        orderitem.save()
    else:

        cart=cartitems.objects.create(user=request.user)
        cart.item.add(orderitem)
    messages.info(request, 'cart item ADD')

    return redirect("cart:cart")

@login_required(login_url='shopping:login')
def deletecartitem(request,id):
    product = get_object_or_404(products, id=id)
    cartitems.objects.filter(item=products, user=request.user).delete()

    messages.info(request, 'cart item deleted')
    return redirect('cart:cart')


def remove_cartitem_qty(request,id):
    product = get_object_or_404(products, id=id)
    orderitem = cartitems.objects.get(item=product, user=request.user)

    if cartitems.objects.filter(item__id=product.id, user=request.user).exists():
        orderitem.quantity -= 1
        orderitem.save()
        if orderitem.quantity==0:
            cartitems.objects.filter(item=product, user=request.user).delete()

    messages.info(request, 'cart item deleted')
    return redirect('cart:cart')


def cart(request):
    data=cartitems.objects.filter(user=request.user)
    gt=0
    for i in data:
        gt+=(i.item.price*i.quantity)

    return render(request,"shopping-cart.html",{'items':data,'gt':gt})