from django.shortcuts import render,redirect
from .models import order_item,address,order,payment
from shopping.models import products,size
from account.models import user_details
from cart.models import cartitems
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
import razorpay

#load checkout view

def checkout(request):
    data=cartitems.objects.filter(user=request.user)
    gt=0
    for i in data:
        gt+=(i.item.price*i.quantity)
    addresses=address.objects.filter(user=request.user)
    return render(request,'check-out.html',{'data':data,'gt':gt,'addresses':addresses})

# add address to user account
@login_required(login_url='shopping:login')
def add_address(request):
    if request.method=="POST":
        addressform =address(user=request.user,
        first_name = request.POST['first_n'],
        last_name = request.POST['last_n'],
        address1 = request.POST['address1'],
        address2 = request.POST['address2'],
        state = request.POST['state'],
        city = request.POST['city'],
        zipcode = request.POST['zip'],
        phone = request.POST['phone'])
        addressform.save()
        return redirect("orders:checkout")
    return render(request,'add_address.html')

def myorders(request):
    if request.method=='POST':
        item = order_item.objects.get(id=request.POST['delete'])
        item.status ="order cancelled"
        item.save()
        return redirect('myorders')
    data=order.objects.filter(user=request.user)
    for i in data:
        orderitem=order_item.objects.filter(orders_id=i.id)
    return render(request,'myorders.html',{'data':orderitem})

#place order (save to orders with process status)
@login_required(login_url='../login')
def placeorder(request):
    if request.method =='POST':
        add=address.objects.get(id=request.POST['addresss'])
        if cartitems.objects.filter(user=request.user).exists():
            orderForm=order(user=request.user,
                    order_date=datetime.date.today(),
                    address=add,
                    order_status="Process")
            orderForm.save() #save details to orders

            orders = orderForm.id
            items = cartitems.objects.filter(user=request.user)
            gt = 0
            for i in items:
                gt += (i.item.price * i.quantity)

            return render(request,"payment.html",{'orders':orders,'gt':gt})
        else:
            messages.info(request, 'Empty cart !!')
            return redirect('cart:cart')
        
        
@login_required(login_url='../login')
def cash_on_delivery(request,slug):
    if cartitems.objects.filter(user=request.user).exists():
        orders=order.objects.get(id=slug)
        items=cartitems.objects.filter(user=request.user)
        gt=0
        for i in items:
            gt += (i.item.price * i.quantity)
            orderItemForm=order_item(orders=orders,
                                     item=i.item,
                                     quantity=i.quantity)
            orderItemForm.save()
        paymentform=payment(orders=orders,
                                amount=gt,
                                type="Cash On Delivery")
        paymentform.save()
    # change order status in order
        orderstatus = orders
        orderstatus.order_status = "Payment Success"
        orderstatus.save()
        cartitems.objects.filter(user=request.user).delete()
        messages.info(request, 'order placed successfully... !!')
        return redirect('/')

    else:
        messages.info(request, 'Empty cart !!')
        return redirect('cart:cart')
@login_required(login_url='shopping:login')
def online_payment(request,slug):
    if cartitems.objects.filter(user=request.user).exists():
        orders=order.objects.get(id=slug)
        items=cartitems.objects.filter(user=request.user)
        gt = 0
        for i in items:
            gt += (i.item.price * i.quantity)
            orderItemForm = order_item(orders=orders,
                                       item=i.item,
                                       quantity=i.quantity)
            orderItemForm.save()
        amount=gt*100
        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_1zrWy3oPfp9cS1', 'OFENWLMA0l9lfLrxGFlW7RZZ'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    receipt=slug,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            paymentform = payment(orders=orders,
                                  amount=gt,
                                  type="Online Payment",
                                  order_id=order_id)
            paymentform.save()

        return render(request,'onlinepayment.html',{'amount':amount,'order_id':order_id})
    else:
        messages.info(request, 'Empty cart !!')
        return redirect('shopping:cart')


def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_1zrWy3oPfp9cS1', 'OFENWLMA0l9lfLrxGFlW7RZZ'))

    try:
        status=client.utility.verify_payment_signature(params_dict)
        # add payment id in payment table
        payments = payment.objects.get(order_id=response['razorpay_order_id'])
        payments.payment_id = response['razorpay_payment_id']
        payments.save()
        # change order status in order table
        orderId=payments.orders.id
        orderstatus=order.objects.get(id=orderId)
        orderstatus.order_status="Payment Success"
        orderstatus.save()
        cartitems.objects.filter(user=request.user).delete()

        messages.info(request, 'order placed successfully... !!')
        return redirect('/')
    except:
        messages.info(request, 'payment Faild... !!')
        return redirect('/')