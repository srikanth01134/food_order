from django.shortcuts import render,redirect
from cart_app.models import cart_model
from crud_app.models import food_model
from django.db.models import Sum,Avg,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/proapp18/login/')
def cart_register(request):
    if request.method=='POST':
        res=cart_model.objects.create(customer_id=request.POST['customer_id'],your_item_id=request.POST['your_item_id'],your_item_name=request.POST['your_item_name'],price=int(float(request.POST['price'])),quantity=request.POST['quantity'],hotel_id=request.POST['hotel_id'],total_price=int(float(request.POST['price']))*int(request.POST['quantity']))
        messages.success(request,"Item is added in cart")
        hotel=request.POST['hotel_id']
        return redirect(f'/proapp18/category_user/{hotel}/')
    else:
        messages.error(request,"Item is not added in cart")



@login_required(login_url='/proapp18/login/')
def cart_view(request,pk):
    res=cart_model.objects.filter(customer_id=request.user.id,hotel_id=pk)
    prod_data=food_model.objects.all()
    total_price=cart_model.objects.filter(customer_id=request.user.id,hotel_id=pk).aggregate(Sum('total_price'))
    return render(request=request,template_name='cart_list.html',context={'res':res,'prod_data':prod_data,'total_price':total_price['total_price__sum'],'hotel_id':pk})
    
@login_required(login_url='/proapp18/login/')
def cart_remove(request,cart_id,hotel_id):
    cart_model.objects.filter(cart_id=cart_id).delete()
    messages.success(request,"item is removed")
    return redirect(f'/cart_app/cart_list/{hotel_id}/')