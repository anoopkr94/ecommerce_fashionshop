from django.shortcuts import render,redirect
from .models import products, wishlists, feedback, category,size,type
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime


def index(request):
    data=products.objects.all()
    return render(request,'index.html',{'data':data})

def faq(request):
    return render(request,'faq.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    data=products.objects.all()
    return render(request,'shop.html',{'data':data})
#show product
def product(request,id):
    data=products.objects.filter(id=id)
    sizes=size.objects.filter(item_id=id)
    for datas in data:
        typ=datas.type
    related=products.objects.filter(type=typ)
    feed=feedback.objects.filter(product_id=id)
    count=0
    for i in feed:
        count+=1
    return render(request,'product.html',{'data':data,'related':related,'feed':feed,'count':count,'sizes':sizes})
#show category based view
def product_s(request,name):
    catName=category.objects.get(name__iexact=name)
    data = products.objects.filter(category=catName)
    return render(request,'shop.html',{'data':data})

def type_shop(request,name):
    typeName=type.objects.get(name__iexact=name)
    data = products.objects.filter(type=typeName)
    return render(request,'shop.html',{'data':data})

@login_required(login_url='login')
def wishlist(request,id):
    pid=products.objects.get(id=id)
    a = wishlists(product=pid,user=request.user)
    a.save()
    messages.info(request, 'item added to wishlist')
    return redirect('shopping:shop')


@login_required(login_url='login')
def wishlist_view(request):
    wish=wishlists.objects.filter(user=request.user)
    return render(request,'wishlist.html',{'wish':wish})

def delete_wishlist(request,id):
    wishlists.objects.filter(id=id,user=request.user).delete()
    messages.info(request, 'wishlist item deleted')
    return redirect('shopping:wishlist_view')

def searchmatch(key,item):
    if key in item.name.lower() or key in item.brand.lower() or key in item.category.name.lower() or key in item.type.name.lower():
        return True
    else:
        return False

def search(request):
    key=request.POST['search']
    protmp=products.objects.all()
    prod=[item for item in protmp if searchmatch(key,item)]
    return render(request,'shop.html',{'data':prod})

def feed(request):

    msg=request.POST['msg']
    id=request.POST['id']
    product=products.objects.get(id=id)

    f=feedback(message=msg,date=datetime.date.today(),product=product,user=request.user)
    f.save()
    return redirect('shopping:product',id)

# Create your views here

