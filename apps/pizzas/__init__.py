from django.db import models


class PizzaStateChoices(models.TextChoices):
    RAW = 'RAW'
    DONE = 'DONE'
