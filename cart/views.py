from django.shortcuts import render,redirect
from .models import cartitem
from shopping.models import products,wishlists
from orders.models import order_details,order_items,payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='login')
def addtocart(request,id):
    if cartitem.objects.filter(pro_id=id,user=request.user).exists():
        item=cartitem.objects.get(pro_id=id,user=request.user)
        item.qty+=1
        item.save()
        item.total=item.price*item.qty
        item.save()
    else:
        datas=products.objects.filter(id=id)
        for data in datas:
            product_id=data.id
            name=data.name
            image=data.image
            seller=data.seller
            price=data.price
            total=price
            a=cartitem(pro_id=product_id,name=name,image=image,seller=seller,user=request.user,price=price,total=total)
            a.save()
        messages.info(request, 'item added to cart')
        return redirect('cart')
    messages.info(request, 'cart updated')
    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    usr=request.user
    data=cartitem.objects.filter(user=usr)
    gt=0
    for datas in data:
        t=datas.total
        gt=gt+t
    return render(request,'shopping-cart.html',{'data':data,'gt':gt})
def delete_cart(request,id):
    cartitem.objects.filter(id=id,user=request.user).delete()
    messages.info(request, 'cart item deleted')
    return redirect('cart')
def delete_qty_cart(request,id):
    if cartitem.objects.filter(pro_id=id,user=request.user).exists():
        item=cartitem.objects.get(pro_id=id,user=request.user)
        item.qty-=1
        item.save()
        item.total=item.price*item.qty
        item.save()
        if item.qty==0:
            cartitem.objects.filter(id=item.id, user=request.user).delete()
        messages.info(request, 'cart updated')
        return redirect('cart')
    messages.info(request, 'cart updated')
    return redirect('cart')
# Create your views here.
