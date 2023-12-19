from django.db import models
class category_model(models.Model):
    category_id=models.AutoField(primary_key=True)
    hotel_id=models.IntegerField()
    category_name=models.CharField(max_length=30)
    category_desc=models.TextField()
    category_image=models.ImageField()
    def __str__(self):
        return self.category_name

    
class food_model(models.Model):
    category_id=models.ForeignKey(category_model,on_delete=models.CASCADE)
    hotel_id=models.IntegerField()
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=30)
    item_price=models.FloatField()
    item_quantity=models.IntegerField(default=1)
    item_desc=models.TextField()
    item_image=models.ImageField()
    