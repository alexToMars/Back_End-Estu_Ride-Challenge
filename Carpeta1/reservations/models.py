from django.db import models

# Create your models here.

class Reservation(models.Model):
    name=models.CharField(max_length=70)
    date=models.DateField()
    numberGuests=models.IntegerField()
