from django import forms 
from proapp18.models import customer_model,hotel_register
from django.contrib.auth.hashers import make_password
import re


class customer_form(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = customer_model
        fields = ['username','first_name','last_name','email','phone','gender','dob','password']

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
    
    def clean_repassword(self):
        pwd = self.cleaned_data['repassword']
        if not (pwd[0].isupper()):
            raise forms.ValidationError('Repassword start with upper char')
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
        if self.cleaned_data['password'] != pwd:
            raise forms.ValidationError('password and repassword should be same')
        return pwd
    

    def save(self, commit = True):
        user = super().save(commit=False)
        if self.cleaned_data['password'] == self.cleaned_data['repassword']:
            user.password = make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user

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

class hotel_register_form(forms.ModelForm):
    class Meta:
        model=hotel_register
        fields='__all__'
