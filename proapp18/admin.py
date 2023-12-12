from django.contrib import admin
from proapp18.models import hotel_register
# Register your models here.
class hotel_admin(admin.ModelAdmin):
    list_display=['id','restarunt_name','restarunt_address','email','phoneno','image']
admin.site.register(hotel_register,hotel_admin)