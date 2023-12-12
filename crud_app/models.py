from django.db import models
from proapp18.models import hotel_register
class category_model(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=30)
    category_desc=models.TextField()
    
class food_model(models.Model):
    hotel_id=models.ForeignKey(hotel_register,on_delete=models.CASCADE)
    category_id=models.ForeignKey(category_model,on_delete=models.CASCADE)
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=30)
    item_price=models.FloatField()
    item_quantity=models.IntegerField()
    item_desc=models.TextField()
    item_image=models.ImageField()
    
    