from django.shortcuts import render,redirect
from proapp18.forms import customer_form,login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
import random
from crud_app.models import category_model,food_model
from owner_app.models import owner_model
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


otp_confirm = None
def login_view(request):
    global otp_confirm
    form = login_form()
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
            print(user)
            if user:
                print(user)
                login(request, user)
                otp = random.randint(0000,9999)
                otp_confirm = otp
                email = user.email
                subject = "Welcome to TCS Company"
                msg =f'''Dear Ncs  Employee,
 
                        Congratulation! 
                        We will provide you work from home job interested candidates send your name address contact details.
                        We are giving you welcome kit at your address by speed post. 
    
                        We think that your experience and skills will be a valuable asset to our company.
                        
                        OTP CONFIRM : {otp}
                        '''
                send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
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
    return render(request=request,template_name='Hotel_home.html',context={'data':res})


def category_user_view(request,pk):
    res=category_model.objects.filter(hotel_id=pk)
    return render(request=request,template_name='customer_cate.html',context={'data':res})


def items_user_view(request,hotel,category):
    res=food_model.objects.filter(hotel_id=hotel,category_id=category)
    print(res)
    return render(request=request,template_name='items_user.html',context={'data':res})


