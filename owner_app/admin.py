from django.contrib import admin
from owner_app.models import owner_model
# Register your models here.


class owner_admin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','phone','gender','dob','restarunt_name','restarunt_address','restarunt_email','restarunt_phoneno','restarunt_location','image','time']

admin.site.register(owner_model,owner_admin)