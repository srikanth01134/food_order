from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class owner_model(User):
    phone = models.PositiveBigIntegerField(unique=True)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female']])
    restarunt_name=models.CharField(max_length=50)
    restarunt_address=models.CharField(max_length=200)
    restarunt_email=models.EmailField(unique=True)
    restarunt_phoneno=models.PositiveBigIntegerField(unique=True)
    restarunt_location=models.CharField(max_length=150,choices=[['punjagutta','punjagutta'],['hitech city','hitech city'],['kphb','kphb']])
    image=models.ImageField()
    time=models.CharField(max_length=50)
    date_of_join=models.DateTimeField(auto_now=True)

