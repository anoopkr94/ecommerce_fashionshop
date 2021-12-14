from django.shortcuts import render,redirect
from .models import order_details,order_items,payment
from shopping.models import products, wishlists
from account.models import user_details
from cart.models import cartitem
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

def checkout(request):
    usr=request.user
    data=cartitem.objects.filter(user=usr)
    gt=0
    for datas in data:
        t=datas.total
        gt=gt+t
    return render(request,'check-out.html',{'data':data,'gt':gt})


def myorders(request):
    if request.method=='POST':
        item = order_items.objects.get(id=request.POST['delete'])
        item.status ="order cancelled"
        item.save()
        return redirect('myorders')
    usr = request.user
    data=order_items.objects.filter(user=usr)
    return render(request,'myorders.html',{'data':data})


def placeorder(request):
    if request.method=='POST':
        user = request.user
        data = cartitem.objects.filter(user=user)
        gt = 0
        for datas in data:
            t = datas.total
            gt = gt + t
        fname = request.POST['fir']
        lname = request.POST['last']
        address = request.POST['add']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['zip']
        mobile = request.POST['phone']
        email = request.POST['email']
        form=order_details(user=user,fname=fname,lname=lname,address=address,state=state,city=city,pin=pin,mobile=mobile,email=email,date=datetime.date.today(),gt=gt)
        form.save()
        return render(request,'payments.html',{'gt':gt})


def payments(request):
    if request.method=='POST':
        user = request.user
        i=order_details.objects.filter(user=user,date=datetime.date.today())
        for d in i:
            order_id = d.id
        item=cartitem.objects.filter(user=user)
        for data in item:
            pro_id=data.pro_id
            name = data.name
            image = data.image
            seller=data.seller
            qty=data.qty
            price = data.price
            total =data.total
            odr=order_items(user=request.user,pro_id=pro_id,name=name,image=image,seller=seller,qty=qty,price=price,total=total,order_id=order_id,status="orderd")
            odr.save()
            product = products.objects.filter(id=pro_id)
            for a in product:
                ps = a.stock
                ps = ps - qty
            product = products.objects.filter(id=pro_id).update(stock=ps)
        data = cartitem.objects.filter(user=user)
        gt = 0
        for datas in data:
            t = datas.total
            gt = gt + t
        name = request.POST['name']
        no = request.POST['number']
        month=request.POST['month']
        year=request.POST['year']
        cvv=request.POST['cvv']
        type="card"
        form=payment(user=request.user,type=type,card_no=no,card_name=name,month=month,year=year,cvv=cvv,amount=gt,order_id=order_id)
        form.save()
        cartitem.objects.filter(user=user).delete()
        messages.info(request, 'Order Placed Succesfully......!')
        return redirect('myorders')
    #save to order items
    user = request.user
    item = cartitem.objects.filter(user=user)
    for data in item:
        pro_id=data.pro_id
        name = data.name
        image = data.image
        seller=data.seller
        qty = data.qty
        price = data.price
        total = data.total
        order_id = data.id
        odr = order_items(user=request.user,pro_id=pro_id, name=name, image=image,seller=seller, qty=qty, price=price, total=total,order_id=order_id,status="orderd")
        odr.save()
        product=products.objects.filter(id=pro_id)
        for a in product:
            ps=a.stock
            ps=ps-qty
        product = products.objects.filter(id=pro_id).update(stock=ps)
    i = order_details.objects.filter(user=user, date=datetime.date.today())
    for d in i:
        order_id = d.id
    data = cartitem.objects.filter(user=request.user)
    gt = 0
    for datas in data:
        t = datas.total
        gt = gt + t
    form=payment(type="COD",user=request.user,amount=gt,order_id=order_id)
    form.save()
    cartitem.objects.filter(user=request.user).delete()
    messages.info(request, 'Order Placed Succesfully......!')
    return redirect('myorders')

# Create your views here.
