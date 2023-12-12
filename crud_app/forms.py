from django import forms
from crud_app.models import category_model,food_model


class category_form(forms.ModelForm):
    class Meta:
        model=category_model
        fields='__all__'



class item_form(forms.ModelForm):
    class Meta:
        model=food_model
        fields='__all__'

    