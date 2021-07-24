from django.db import models


# Create your models here.
class Pizza(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    name = models.CharField(max_length=128, blank=False)
    cheese = models.CharField(max_length=128, default='')
    pastry = models.CharField(max_length=128, default='')
    secret_ingredient = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.name
