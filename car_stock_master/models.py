from django.db import models

# Create your models here.

class car_stock(models.Model):
    # pictures_of_car
    car_brand=models.CharField(max_length=100)
    car_price=models.FloatField()
    car_model=models.IntegerField(max_length=100)
    model_year=models.IntegerField()
    # fuel_type(petrol / diesel)
    # car_type(manual / automatic)
    # car_state=models.IntegerField(max_length=100)
    car_history=models.IntegerField(max_length=100)
    kilometers_driven=models.FloatField()
    last_service=models.DateField()
    owner=models.CharField(max_length=100)
    # insurance=
    # body_structure=
    sale_status=models.IntegerField(max_length=100)
