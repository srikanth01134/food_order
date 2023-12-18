from django.shortcuts import render,redirect
from owner_app.forms import owner_form,login_form,change_password_form
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
import random
from owner_app.models import owner_model
from crud_app.models import category_model
# Create your views here.



pk=None

#password and mail sending to
def owner_register_view(request):
    global pk
    pk=request.user.pk
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
            return redirect(f'/owner_app/sub_login_view/{pk}/')
    return render(request=request,template_name='owner_register.html',context={'form':form})
#change password views

def owner_login_view(request):
    form=login_form()
    if request.method=="POST":
        form =login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username = username,password = password)
            if user:
                login(request,user)
                return redirect(f'/owner_app/sample_home_view/')
            else:
                messages.error(request,'you enter the wrong password or username')
    return render(request,'owner_login.html',context={'form':form})
            
otp_confirm=None
def change_pass_view(request,pk):
    global otp_confirm
    form=change_password_form()
    if request.method=='POST':
        res =owner_model.objects.get(id=pk)
        form=change_password_form(request.POST)
        if form.is_valid():
            if form.cleaned_data['Enter_password']==form.cleaned_data['Re_Enter_password']:
                owner_model.objects.filter(id=pk).update(password=make_password(form.cleaned_data['Enter_password']))
                if res:
                    print(res)
                    if res.is_staff:
                        otp = random.randint(0000,9999)
                        otp_confirm = otp
                        email = res.email
                        subject = "Welcome to Hotel management"
                        msg =f'''Dear {request.user},
                                Congratulation! 
                                We are provide you OTP details.                        
                                OTP CONFIRM : {otp}
                                                '''
                    send_mail(subject=subject,message=msg,from_email = settings.EMAIL_HOST_USER, recipient_list=[email,])
                    login(request, res)  
                    return redirect(f'/owner_app/otp_view/{pk}/')
    return render(request=request,template_name='change_password.html',context={'form':form})


def otp_view(request,pk):
    if request.method == 'POST':
        if str(otp_confirm) == str(request.POST['otp_confirm']):
            messages.success(request,'Password change is success')
            return redirect(f'/owner_app/sample_home_view/{pk}/')
        else:
            logout(request)
            messages.success(request,"otp entered is incorrect")
            return redirect(f'/owner_app/sub_login_view/{pk}/')
    return render(request=request, template_name='owner_otp.html')

 
 
def sample_home_view(request):
    res=category_model.objects.all()
    print(request.user.id)
    return render(request,'sample.html',context={'res':res})



def sub_login_view(request):
    form=login_form()
    if request.method=="POST":
        form =login_form(request.POST)
        if form.is_valid():
            user=owner_model.objects.get(id=pk)
            print(user)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username)
            print(password)
            user=authenticate(username = username,password = password)
            if user:
                login(request,user)
                return redirect(f'/owner_app/change_pass_view/{pk}')
            else:
                messages.error(request,'you enter the wrong password or username')
    return render(request,'sub_login.html',context={'form':form})
@login_required(login_url='/owner_app/sub_login_view/')
def logout_view(request):
    logout(request)
    return redirect('/owner_app/sub_login_view/')