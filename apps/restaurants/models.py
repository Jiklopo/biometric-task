from datetime import date
from django.db import models
from rest_framework.exceptions import ValidationError


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(
        max_length=128,
        blank=True,
        default=''
    )

    description = models.TextField(
        blank=True,
        default=''
    )

    date_opened = models.DateField(null=True)

    rating = models.FloatField(default=0)

    def clean(self):
        if not 0 <= self.rating <= 5:
            raise ValidationError('Rating must be between 0 and 5!')
        if self.date_opened:
            if (date.today() - self.date_opened).days < 0:
                raise ValidationError('Opening Date cannot be in the futures!')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}({self.id})'
