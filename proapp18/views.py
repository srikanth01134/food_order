from django.shortcuts import render,redirect
from proapp18.forms import customer_form,login_form,customer_update,customer_change_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
import random
from crud_app.models import category_model,food_model
from owner_app.models import owner_model
from proapp18.models import customer_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.


def start_view(request):
    return render(request,'index.html')

def customer_register(request):
    form = customer_form()
    if request.method == 'POST':
        form = customer_form(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            subject = "Welcome to TCS Company"
            msg = '''Dear Ncs  Employee,
                    Congratulation! 
                    We will provide you work from home job interested candidates send your name address contact details.
                    We are giving you welcome kit at your address by speed post. 
 
                    We think that your experience and skills will be a valuable asset to our company.
                    '''
            send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
            return redirect('/proapp18/login/')
    return render(request=request,template_name='register.html',context={'form':form})



def customer_update_view(request,pk):
    res=customer_model.objects.get(id=pk)
    form = customer_update(instance=res)
    if request.method == 'POST':
        res=customer_model.objects.get(id=pk)
        form = customer_update(request.POST,instance=res)
        if form.is_valid:
            form.save()
            return redirect('/proapp18/home/')
        else:
            return HttpResponse('not saved')
    return render(request=request,template_name='profile.html',context={'form':form})


otp_confirm = None
def login_view(request):
    global otp_confirm
    form = login_form()
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user:
                login(request, user)
                otp = random.randint(0000,9999)
                otp_confirm = otp
                email = user.email
                print(email)
                subject = "Welcome to TCS Company"
                msg =f'''Dear Ncs  Employee,
 
                        Congratulation! 
                        We will provide you work from home job interested candidates send your name address contact details.
                        We are giving you welcome kit at your address by speed post. 
    
                        We think that your experience and skills will be a valuable asset to our company.
                        
                        OTP CONFIRM : {otp}
                        '''
                send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
                print('hai')
            return redirect('/proapp18/otp/')
    return render(request=request,template_name='login.html',context={'form':form})


def otp_view(request):
    if request.method == 'POST':
        if str(otp_confirm) == str(request.POST['otp_confirm']):
            return redirect('/proapp18/home')
        else:
            logout(request)
            return redirect('/proapp18/login/')
    return render(request=request, template_name='otp_genrate.html')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/proapp18/login')

@login_required(login_url='/login')
def home_view(request):
    res=owner_model.objects.all()
    # data=category_model.objects.all()
    return render(request=request,template_name='Hotel_home.html',context={'data':res})


def category_user_view(request,pk):
    res=category_model.objects.filter(hotel_id=pk)
    return render(request=request,template_name='customer_cate.html',context={'data':res,'hotel_id':pk})


def items_user_view(request,hotel,category):
    res=food_model.objects.filter(hotel_id=hotel,category_id=category)
    return render(request=request,template_name='items_user.html',context={'data':res})


otp_confirm=None
def forget_password_view(request):
    res=customer_model.objects.all().values_list('email')
    print(res)
    global otp_confirm
    if request.method =='POST':
        otp=random.randint(000000,999999)
        otp_confirm=otp
        email=request.POST['email']
        print(request.POST)
        if (email,) in res :
            subject='customer verifivcation code for the password change'
            msg=f'''DEar customer plese enter
                the otp {otp}
                change the password 
                Thank you for your verification'''
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
            email_id=customer_model.objects.get(email=email)
            return redirect(f'/proapp18/customer_otp/{email_id.id}/')
        else:
            messages.error(request,'otp is incorrect')
    return render(request,'customer_forget.html')


def customer_otp_view(request,pk):
    if request.method == 'POST':
        if str(otp_confirm) == str(request.POST['otp_confirm']):
            return redirect(f'/proapp18/change_pass/{pk}/')
        else:
            logout(request)
            return redirect('/proapp18/customer_forget/')
    return render(request=request, template_name='customer_otp.html')


def change_pass_view(request,pk):
    form=customer_change_form()
    if request.method=='POST':
        form=customer_change_form(request.POST)
        if form.is_valid():
            if form.cleaned_data['Enter_password']==form.cleaned_data['Re_Enter_password']:
                customer_model.objects.filter(id=pk).update(password=make_password(form.cleaned_data['Enter_password']))
                messages.success(request,'password change successful')
                return redirect('/proapp18/login/')
    return render(request=request,template_name='change_password.html',context={'form':form})