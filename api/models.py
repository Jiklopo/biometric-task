from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from .validators import validate_iin, not_future
from datetime import datetime


class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    date_opened = models.DateField(null=True, validators=[not_future])
    rating = models.FloatField(default=0, validators=[
        MinValueValidator(0, 'Rating must be greater than 0!'),
        MaxValueValidator(5, 'Rating must be 5 or lower!')
    ])

    def __str__(self):
        return f'{self.name}({self.id})'


class Staff(models.Model):
    class JobTextChoices(models.TextChoices):
        WAITER = 'WTR'
        CLEANER = 'CLN'
        COOK = 'CK'
        GUARD = 'GRD'

    class GenderTextChoices(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        FIGHT_HELICOPTER = 'H'
        UNKNOWN = 'U'

    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.TextField(validators=[EmailValidator])
    gender = models.CharField(max_length=1, choices=GenderTextChoices.choices)
    job = models.CharField(max_length=3, choices=JobTextChoices.choices)
    birth_date = models.DateField(validators=[not_future])
    date_joined = models.DateField(validators=[not_future])

    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.id})@{self.restaurant}'


class Pizza(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    cheese = models.CharField(max_length=128, blank=True)
    pastry = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name
