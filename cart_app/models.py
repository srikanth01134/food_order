from django.db import models

# Create your models here.


class cart_model(models.Model):
    cart_id=models.AutoField(primary_key=True)
    customer_id=models.PositiveIntegerField()
    hotel_id=models.PositiveIntegerField()
    customer_name=models.CharField(max_length=110)
    your_item_id=models.IntegerField()
    your_item_name=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()
