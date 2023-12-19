from django import forms
from crud_app.models import category_model,food_model


class category_form(forms.ModelForm):
    class Meta:
        model=category_model
        exclude=['hotel_id']



class item_form(forms.ModelForm):
    class Meta:
        model=food_model
        exclude=['hotel_id','item_quantity']


    def __init__(self,*args,**kwargs):
        hotel=kwargs.pop('hotel',None)
        super(item_form,self).__init__(*args,**kwargs)
        self.fields['category_id']=forms.ModelChoiceField(queryset=category_model.objects.filter(hotel_id=hotel))

class items_update_form(forms.ModelForm):
    class Meta:
        model=food_model
        exclude=['category_id','hotel_id','item_quantity']   


    