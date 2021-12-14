from django.shortcuts import render,redirect
from account.models import user_details
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            type_obj = user_details.objects.get(user=username)

            if user.is_authenticated and type_obj.type=="user":

                return render(request,'index.html')

            elif user.is_authenticated and type_obj.type=="seller":

                return render(request,'seller_home.html')
        else:
            messages.info(request,'invalid username or password')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['repassword']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=name)
                user.save()
                typ=user_details(type="user",user=username)
                typ.save()
                return render(request,'login.html')
    return render(request,'register.html')

def reg_seller(request):
    if request.method=='POST':
        name = request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['repassword']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=name)
                user.save()
                typ=user_details(type="seller",user=username)
                typ.save()
                return render(request,'login.html')
    return render(request,'register_seller.html')

def forget_pswd(request):
    if request.method=='POST':
        messages.info(request, 'PAssword Reset Link Send To Your Email')
        return render(request,'forget_pswd.html')
    return render(request,'forget_pswd.html')
# Create your views here.
