from django.shortcuts import render,redirect
from crud_app.models import category_model,food_model
from crud_app.forms import category_form,item_form
# Create your views here.
def catagory_view(request):
    form=category_form()
    if request.method=='POST':
        form=category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')
    return render(request,'category.html',context={'form':form})

def display(request):
    res=category_model.objects.all()
    return render(request,'display.html',context={'data':res})

def updates(request,pk):
    res=category_model.objects.get(category_id=pk)
    form=category_form(instance=res)
    if request.method=='POST':
        form=category_form(request.POST,instance=res)
        if form.is_valid():
            form.save()
        return redirect('/display')
    return render(request,'update.html',context={'data':res})

def deletes(request,pk):
    res=category_model.objects.get(category_id=pk)
    if request.method=='POST':
        res=category_model.objects.get(category_id=pk).delete()
        return redirect('/display')
    return render(request,'delete.html',context={'data':res})


#items for  category
def items_view(request):
    form=item_form()
    if request.method=='POST' and request.FILES:
        form=item_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/crud_app/items_list')
    return render(request,'items.html',context={'form':form})


def items_list(request):
    res=food_model.objects.all()
    return render(request,'items_list.html',context={'data':res})


def item_update(request,pk):
    res=food_model.objects.get(item_id=pk)
    form=item_form(instance=res)
    if request.method=='POST'  and request.FILES:
        form=item_form(request.POST,request.FILES,instance=res)
        if form.is_valid():
            form.save()
        return redirect('/crud_app/items_list')
    return render(request,'items_update.html',context={'data':res})

def item_delete(request,pk):
    res=food_model.objects.get(item_id=pk)
    if request.method=='POST':
        res=food_model.objects.get(item_id=pk).delete()
        return redirect('/crud_app/items_list')
    return render(request,'items_delete.html',context={'data':res})


def non_view(request):
    return render(request,'non_veg.html')