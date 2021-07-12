from django.core.exceptions import ValidationError
import datetime


def validate_iin(value):
    if len(value) != 12:
        raise ValidationError(
            f'{value} length must be 12'
        )


def not_future(value):
    td = datetime.date.today() - value
    if td.days < 0:
        raise ValidationError(f'{value} is in the future!')
