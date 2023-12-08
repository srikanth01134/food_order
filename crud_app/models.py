from django.db import models

class category_model(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=30)
    category_desc=models.TextField()
    
# class food_model(models.Model):
#     category_id=models.ForeignKey(category_model,on_delete=models.CASCADE)
#     item_id=models.AutoField(primary_key=True)
#     item_name=models.CharField(max_length=30)
#     item_price=models.FloatField()
#     item_quantity=models.IntegerField()
#     item_desc=models.TextField()
    