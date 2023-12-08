from django.shortcuts import render,redirect
from crud_app.models import category_model,food_model
# Create your views here.
def catagory_view(request):
    if request.method=='POST':
        print(request.POST)
        category_model.objects.create(category_name=request.POST['category_name'],
                                      category_desc=request.POST['category_desc'],)
                                    
        return redirect('/crud_app/display')
    return render(request,'category.html')

def display(request):
    res=category_model.objects.all()
    return render(request,'display.html',context={'data':res})

def updates(request,pk):
    res=category_model.objects.get(category_id=pk)
    if request.method=='POST':
        print(request.POST)
        category_model.objects.filter(cat_id=pk).update(catcategory_name=request.POST['category_name'],
                                                    category_desc=request.POST['catcategory_desc'])
        return redirect('/crud_app/display')
    return render(request,'update.html',context={'data':res})

def deletes(request,pk):
    res=category_model.objects.get(category_id=pk)
    if request.method=='POST':
        res=category_model.objects.get(category_id=pk).delete()
    return render(request,'delete.html',context={'data':res})

def veg(request):
    return render(request=request,template_name='veg_page.html')




#items for  category
def items_view(request):
    item=category_model.objects.all()
    if request.method=='POST':
        print(request.POST)
        food_model.objects.create(category_id_id=request.POST['category_id'],
                                    item_name=request.POST['item_name'],
                                    item_price=request.POST['item_price'],
                                    item_quantity=request.POST['item_quantity'],
                                    item_desc=request.POST['item_desc'])
        return redirect('/crud_app/items_list')
    return render(request,'items.html',context={'item':item})


def items_list(request):
    res=food_model.objects.all()
    return render(request,'items_list.html',context={'data':res})


def item_update(request,pk):
    res=food_model.objects.get(item_id=pk)
    if request.method=='POST':
        print(request.POST)
        food_model.objects.filter(item_id=pk).update(
        item_name=request.POST['item_name'],
        item_desc=request.POST['item_desc'],
        item_quantity=request.POST['item_quantity'],
        item_price=request.POST['item_price'])
        return redirect('/crud_app/items_list')
    return render(request,'items_update.html',context={'data':res})

def item_delete(request,pk):
    res=food_model.objects.get(item_id=pk)
    if request.method=='POST':
        res=food_model.objects.get(item_id=pk).delete()
        return redirect('/crud_app/items_list')
    return render(request,'items_delete.html',context={'data':res})