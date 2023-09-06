from django.db import models

# Create your models here.


class Auto(models.Model):
    auto_model = models.CharField(max_length=15)
    auto_country = models.CharField(max_length=20)
    auto_year = models.IntegerField()
    auto_number = models.CharField(max_length=10)