from django.db import models

# Create your models here.

class income(models.Model):
    where = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.CharField(max_length=50)
    type = models.CharField(max_length=50)