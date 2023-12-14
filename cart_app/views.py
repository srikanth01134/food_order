from django.shortcuts import render,redirect
from cart_app.models import cart_model
from crud_app.models import food_model
from django.db.models import Sum,Avg,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/crud_app/login')
def cart_register(request,your_item_id,your_item_name,customer_id,price,quantity):
    print(your_item_id,customer_id)
    price=int(float(price))
    res=cart_model.objects.create(customer_id=customer_id,your_item_id=your_item_id,your_item_name=your_item_name,price=price,quantity=quantity)
    print(res.cart_id)
    messages.success(request,"Item is added in cart")
    return redirect('/crud_app/items_list/')


@login_required(login_url='/crud_app/login')
def cart_view(request):
    res=cart_model.objects.filter(customer_id=request.user.id)
    prod_data=food_model.objects.all()
    print(prod_data)
    total_price=cart_model.objects.filter(customer_id=request.user.id).aggregate(Sum('price'))
    return render(request=request,template_name='cart_list.html',context={'res':res,'prod_data':prod_data,'total_price':total_price})
    
@login_required(login_url='/crud_app/login')
def cart_remove(request,cart_id):
    cart_model.objects.filter(cart_id=cart_id).delete()
    messages.success(request,"item is removed")
    return redirect('/cart_app/cart_list')