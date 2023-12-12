from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer_model(User):
    phone = models.PositiveBigIntegerField()
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female']])

class hotel_register(models.Model):
    id=models.IntegerField(primary_key=True)
    restarunt_name=models.CharField(max_length=50)
    restarunt_address=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phoneno=models.PositiveBigIntegerField(unique=True)
    image=models.ImageField()
    time=models.IntegerField()

class hotel_rating(models.Model):
    hotel_id=models.IntegerField()
    rating=models.CharField(max_length=2,choices=[['1','1'],['2','2'],['3','3'],['4','4'],['5','5']])
    comments=models.TextField(null=True)



