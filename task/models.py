from django.db import models

# Create your models here.
class Prices(models.Model):
    # date_from = models.DateField()
    date= models.DateTimeField()
    origin_code = models.CharField(max_length=100)
    destination_code = models.CharField(max_length=100)
    price = models.IntegerField()
    

