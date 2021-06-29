from django.core.exceptions import ValidationError


def validate_iin(value):
    if len(value) != 12:
        raise ValidationError(
            f'{value} length must be 12'
        )
