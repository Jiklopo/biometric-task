from django.db import models

from apps.pizzas import PizzaStateChoices


class Pizza(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    name = models.CharField(max_length=128, blank=False)
    cheese = models.CharField(max_length=128, default='')
    pastry = models.CharField(max_length=128, default='')
    secret_ingredient = models.CharField(max_length=128, default='')

    cooking_time = models.FloatField(default=10)

    state = models.CharField(
        max_length=4,
        choices=PizzaStateChoices.choices,
        default='RAW'
    )

    def __str__(self):
        return self.name
