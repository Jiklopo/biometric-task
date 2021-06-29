from django.db import models


# Create your models here.
class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)


class Pizza(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    cheese = models.CharField(max_length=128, blank=True)
    pastry = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)
