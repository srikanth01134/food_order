from django import forms
from owner_app.models import  owner_model
from django.contrib.auth.hashers import make_password
import re
from owner_app.validators import clean_Enter_password
class owner_form(forms.ModelForm):
    class Meta:
        model=owner_model
        fields=['username','first_name','last_name','email','phone','gender','dob','restarunt_name','restarunt_address','restarunt_email','restarunt_phoneno','restarunt_location','image','time']
     
    def clean_username(self):
        username = self.cleaned_data['username']
        if not (username[0].isupper()):
            raise forms.ValidationError('Username start with Upper')
        if len(username) < 3:
            raise forms.ValidationError('username min 3 char')
        if len(username) > 15:
            raise forms.ValidationError('username max 15 char')
        return username
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) != 10:
            raise forms.ValidationError('check the Phone Number')
        if str(phone)[0] not in '9876':
            raise forms.ValidationError('start with 9,8,7,6')
        return phone
        


class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not (username[0].isupper()):
            raise forms.ValidationError('Username start with Upper')
        if len(username) < 3:
            raise forms.ValidationError('username min 3 char')
        if len(username) > 15:
            raise forms.ValidationError('username max 15 char')
        return username
    
    def clean_password(self):
        pwd = self.cleaned_data['password']
        if len(pwd) < 4:
            raise forms.ValidationError('password min 4 char')
        if len(pwd) > 15:
            raise forms.ValidationError('password max 15 char')
        if len(re.findall('[0-9]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 Numeric')
        if len(re.findall('[^0-9a-zA-Z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 Special char')
        if len(re.findall('[a-z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 lower case')
        if len(re.findall('[A-Z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 upper case')
        return pwd



class change_password_form(forms.Form):
    Enter_password=forms.CharField(widget=forms.PasswordInput,validators=[clean_Enter_password])
    Re_Enter_password=forms.CharField(widget=forms.PasswordInput)
        
    def clean_Re_Enter_password(self):
        pwd = self.cleaned_data['Re_Enter_password']
        if len(pwd) < 4:
            raise forms.ValidationError('password min 4 char')
        if len(pwd) > 15:
            raise forms.ValidationError('password max 15 char')
        if len(re.findall('[0-9]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 Numeric')
        if len(re.findall('[^0-9a-zA-Z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 Special char')
        if len(re.findall('[a-z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 lower case')
        if len(re.findall('[A-Z]', pwd)) == 0:
            raise  forms.ValidationError('altest 1 upper case')
        return pwd

        