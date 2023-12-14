from django.shortcuts import render,redirect
from owner_app.forms import owner_form,login_form
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
import random
# Create your views here.

def owner_register_view(request):
    form = owner_form()
    if request.method == 'POST' and request.FILES:
        form = owner_form(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            name=form.cleaned_data['username'][0:4]+"$"+str(form.cleaned_data['phone'])[0:4]
            print(name)
            user.password = make_password(name)
            user.is_staff=True
            if user:
                user.save()
                subject = "Welcome to Hostel management"
                msg = f'''Dear {username},
                        Congratulation! 
                        We are provide you Login details.
                        username={username}
                        password={name}
                        We are giving you welcome wishes.
                        Please Login from website and Change the password.
                        '''
                send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
    return render(request=request,template_name='owner_register.html',context={'form':form})

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
                if user.is_staff:
                    otp = random.randint(0000,9999)
                    otp_confirm = otp
                    email = user.email
                    subject = "Welcome to Hotel management"
                    msg =f'''Dear {request.user},
                            Congratulation! 
                            We are provide you OTP details.                        
                            OTP CONFIRM : {otp}
                            '''
                    send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
                    login(request, user)  
                    print("haii")  
                    return redirect('/owner_app/otp_view')
            else:
                messages.error(request,'username and password is incorrect ')
    return render(request=request,template_name='login.html',context={'form':form})

def otp_view(request):
    if request.method == 'POST':
        if str(otp_confirm) == str(request.POST['otp_confirm']):
            messages.success(request,'Login success ')
            return redirect('/proapp18/home')
        else:
            print("hello")
            logout(request)
            return redirect('/owner_app/owner_login')
    return render(request=request, template_name='otp_genrate.html')