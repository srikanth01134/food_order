from django import forms
import re 

def clean_Enter_password(newpwd):
    if len(newpwd) < 4:
            raise forms.ValidationError('password min 4 char')
    if len(newpwd) > 15:
            raise forms.ValidationError('password max 15 char')
    if len(re.findall('[0-9]', newpwd)) == 0:
            raise  forms.ValidationError('altest 1 Numeric')
    if len(re.findall('[^0-9a-zA-Z]', newpwd)) == 0:
            raise  forms.ValidationError('altest 1 Special char')
    if len(re.findall('[a-z]', newpwd)) == 0:
            raise  forms.ValidationError('altest 1 lower case')
    if len(re.findall('[A-Z]', newpwd)) == 0:
        raise  forms.ValidationError('altest 1 upper case')
    return newpwd