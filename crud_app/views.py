from django.shortcuts import render,redirect
from crud_app.models import category_model
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
