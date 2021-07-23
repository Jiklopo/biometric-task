from datetime import date
from django.db import models
from rest_framework.exceptions import ValidationError

from . import GenderTextChoices, JobTextChoices


# Create your models here.
class Staff(models.Model):
    iin = models.CharField(max_length=12, primary_key=True)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GenderTextChoices.choices)
    job = models.CharField(max_length=3, choices=JobTextChoices.choices)

    email = models.EmailField()

    birth_date = models.DateField()
    date_joined = models.DateField()

    def clean(self):
        today = date.today()
        if (today - self.birth_date).days < 0:
            raise ValidationError('Birth date cannot be in the future!')
        if (today - self.date_joined).days < 0:
            raise ValidationError('Joined date cannot be in the future!')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.id})@{self.restaurant}'

    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365.25
