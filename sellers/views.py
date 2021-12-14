from django.shortcuts import render,redirect
from shopping.models import products,category,type
from orders.models import order_items
from .forms import add_item_form, add_type_form, add_size_form


#seller views
def seller_home(request):

    return render(request,'seller_home.html')

def add_category(request):
    catfrm = add_type_form
    if request.method=='POST':
        cat=category(name=request.POST['category'])
        cat.save()
    return render(request,'add_cat_type.html',{'catfrm':catfrm})

def add_type(request):
    if request.method=='POST':
        typ=add_type_form(request.POST)
        if typ.is_valid():
            typ.save()
    return redirect('add_category')

def order_status(request,id):
    if request.method=='POST':
        status=request.POST['status']
        item = order_items.objects.get(id=id)
        item.status=status
        item.save()
        return redirect('seller_order')


def seller_add(request):
    form=add_item_form
    form_size=add_size_form
    if request.method == 'POST':
        form1=add_item_form(request.POST)
        if form1.is_valid():
            form1.save()

        else:
            print("!!!!!!!")
        return redirect('seller_add')
    return render(request,'seller_additems.html',{'form':form,'form_size':form_size})


def seller_view(request):
    user=request.user
    data = products.objects.filter(seller=user)
    return render(request, 'seller_view.html', {'data': data})


def delete_item(request):
    products.objects.filter(id=request.POST['delete_item']).delete()
    return redirect('seller_view')


def seller_order(request):
    user = request.user
    data = order_items.objects.filter(seller=user)
    return render(request, 'seller_orders.html', {'data': data})
# Create your views here.
# AJAX
def load_types(request):
    category_id = request.GET.get('category_id')
    types = type.objects.filter(category_id=category_id).all()
    return render(request, 'type_dropdown_list_options.html', {'types': types})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)