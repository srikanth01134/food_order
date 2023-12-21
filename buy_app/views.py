from django.shortcuts import render,redirect
from buy_app.models import buy_model,buyed_item_list
from django.contrib import messages
from cart_app.models import cart_model
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
def buy_register(request,total_price):
    if request.method == 'POST':
        print("haii")
        buy=buy_model.objects.create(customer_id=request.user.id,total_price=total_price,customer_name=request.POST['username'],customer_phoneno=request.POST['phone'],customer_address=request.POST['Address'],)
        res=cart_model.objects.filter(customer_id=request.user.id).values()
        for i in res:
            buyed_item_list.objects.create(buy_id=buy.buy_id,item_id=i['your_item_id'],item_name=i['your_item_name'],item_price=i['price'],quantity=i['quantity'])
           
        cart_model.objects.filter(customer_id=request.user.id).delete()
        return redirect(f'/buy_app/order_details/{buy.buy_id}/')
    return render(request=request,template_name='buy_confirm.html')

def buy_view(request):
    prod_data=cart_model.objects.all()
    total_price=cart_model.objects.filter(customer_id=request.user.id).aggregate(Sum('price'))
    return render(request,'buy_list.html',context={'prod_data':prod_data,'total_price':total_price})

def order_details(request,buy_id):
    cust_details=buy_model.objects.filter(customer_id=request.user.id,buy_id=buy_id)
    items_details=buyed_item_list.objects.filter(buy_id=buy_id)
    return render(request,'order_details.html',context={'cust_details':cust_details,'items_details':items_details,})

def order_details_view(request):
    cust_details=buy_model.objects.filter(customer_id=request.user.id)
    items_details=buyed_item_list.objects.all()
    return render(request,'order_details.html',context={'cust_details':cust_details,'items_details':items_details,})



