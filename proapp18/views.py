from django.shortcuts import render,redirect
from proapp18.forms import customer_form,login_form,hotel_register_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
import random
from proapp18.models import hotel_register
# Create your views here.


def start_view(request):
    return render(request,'start.html')

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
 
                    We are pleased to confirm that you have been selected to work for our company we are delighted to make you the following job offer as a DATA ENTRY OPERATOR.
 
                    we are glad to inform you that your resume has been selected for the job.  we are confident and look forward to working with you.  Please confirm your acceptance of this offer 
 
                    We will provide you work from home job interested candidates send your name address contact details.
                    We are giving you welcome kit at your address by speed post. 
 
                    We think that your experience and skills will be a valuable asset to our company.
                    '''
            send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
            return redirect('/proapp18/login')
    return render(request=request,template_name='register.html',context={'form':form})


otp_confirm = None

def login_view(request):
    global otp_confirm
    form = login_form
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
            if user:
                login(request, user)
                otp = random.randint(0000,9999)
                otp_confirm = otp
                email = user.email
                subject = "Welcome to TCS Company"
                msg =f''''Dear Ncs  Employee,
 
                        Congratulation! 
    
                        We are pleased to confirm that you have been selected to work for our company we are delighted to make you the following job offer as a DATA ENTRY OPERATOR.
    
                        we are glad to inform you that your resume has been selected for the job.  we are confident and look forward to working with you.  Please confirm your acceptance of this offer 
    
                        We will provide you work from home job interested candidates send your name address contact details.
                        We are giving you welcome kit at your address by speed post. 
    
                        We think that your experience and skills will be a valuable asset to our company.
                        
                        OTP CONFIRM : {otp}
                        '''
                send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
            return redirect('/proapp18/otp')
    return render(request=request,template_name='login.html',context={'form':form})


def otp_view(request):
    if request.method == 'POST':
        if str(otp_confirm) == str(request.POST['otp_confirm']):
            return redirect('/proapp18/home')
        else:
            logout(request)
            return redirect('/proapp18/login')
    return render(request=request, template_name='otp_genrate.html')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/proapp18/login')

@login_required(login_url='/login')
def home_view1(request):
    return render(request=request,template_name='home.html')


@login_required(login_url='/login')
def home_view(request):
    res=hotel_register.objects.all()
    return render(request=request,template_name='Hotel_home.html',context={'data':res})

def hotel1_view(request):
    return render(request=request,template_name='hotel1.html')


def hotel_view(request):
    form=hotel_register_form()
    if request.method=='POST' and request.FILES:
        form=hotel_register_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/proapp18/hotel_display')
    return render(request,'hotel_register.html',context={'form':form})

def hotel_display(request):
    res=hotel_register.objects.all()
    return render(request,'hotel_display.html',context={'res':res})

def hotel_update(request,pk):
    res=hotel_register.objects.get(id=pk)
    form=hotel_register_form(instance=res)
    if request.method=='POST' and request.FILES:
        form=hotel_register_form(request.POST,request.FILES,instance=res)
        if form.is_valid():
            form.save()
            return redirect('/proapp18/hotel_display')
    return render(request,'hotel_update.html',context={'form':form})

def hotel_delete(request,pk):
    res=hotel_register.objects.get(id=pk)
    if request.method=='POST':
         res=hotel_register.objects.get(id=pk).delete()
         return redirect('/proapp18/hotel_display')
    return render(request,'hotel_delete.html',context={'res':res})