from django.shortcuts import render,redirect
from crud_app.models import category_model,food_model
from crud_app.forms import category_form,item_form,items_update_form
from django.contrib import messages
# Create your views here.
def catagory_view(request):
    form=category_form()
    if request.method=='POST' and request.FILES:
        form=category_form(request.POST,request.FILES)
        if form.is_valid():
            if request.user.is_staff:
                data=form.save(commit=False)
                data.hotel_id=request.user.id
                if data:
                    data.save()
                    messages.success(request,'category is created')
                    return redirect('/crud_app/display')
            else:
                messages.error(request,'You are not a owner')
    return render(request,'category.html',context={'form':form})

def display(request):
    res=category_model.objects.filter(hotel_id=request.user.id)
    return render(request,'display.html',context={'form':res})

def updates(request,pk):
    res=category_model.objects.get(category_id=pk)
    form=category_form(instance=res)
    if request.method=='POST' and request.FILES:
        form=category_form(request.POST,request.FILES,instance=res)
        if form.is_valid():
            if request.user.is_staff:
                form.save()
                messages.success(request,'category is updated')
                return redirect('/crud_app/display')
            else:
                messages.error(request,'You are not a owner')
    return render(request,'update.html',context={'form':form})

def deletes(request,pk):
    res=category_model.objects.get(category_id=pk)
    if request.method=='POST':
        if request.user.is_staff:
            res=category_model.objects.get(category_id=pk).delete()
            messages.success(request,'category is deleted')
            return redirect('/crud_app/display')
        else:
            messages.error(request,'You are not a owner')
    return render(request,'delete.html',context={'form':res})


#items for  category
def items_view(request):
    form=item_form(hotel=request.user.id)
    if request.method=='POST' and request.FILES:
        form=item_form(request.POST,request.FILES,hotel=request.user.id)
        if form.is_valid():
            if request.user.is_staff:
                data=form.save(commit=False)
                data.hotel_id=request.user.id
                if data:
                    data.save()
                    messages.success(request,'item is created')
                else:
                    messages.error(request,'You are not a owner')
                return redirect('/crud_app/items_list')
    return render(request,'items.html',context={'form':form})



def items_list(request):
    res=food_model.objects.filter(hotel_id=request.user.id)
    return render(request,'items_list.html',context={'form':res})


def item_update(request,pk):
    res=food_model.objects.get(item_id=pk)
    form=items_update_form(instance=res)
    if request.method=='POST' or request.FILES:
        form=items_update_form(request.POST,request.FILES,instance=res)
        if form.is_valid():
            if request.user.is_staff:
                form.save()
                messages.success(request,'item is updated')
            else:
                messages.error(request,'You are not a owner')
            return redirect('/crud_app/items_list')
    return render(request,'items_update.html',context={'form':form})

def item_delete(request,pk):
    res=food_model.objects.get(item_id=pk)
    if request.method=='POST':
        if request.user.is_staff:
            res=food_model.objects.get(item_id=pk).delete()
            messages.success(request,'item is deleted')
            return redirect('/crud_app/items_list')
        else:
            messages.error(request,'You are not a owner')

    return render(request,'items_delete.html',context={'form':res})


def details_view(request,pk):
    res=food_model.objects.filter(category_id=pk,hotel_id=request.user.id)
    return render(request=request,template_name='items_details.html',context={'res':res})


