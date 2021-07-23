from rest_framework import exceptions

from datetime import date

from apps.staff.models import Staff
from apps.staff.selectors import get_staff


def create_staff(**kwargs):
    iin = kwargs.get('iin')
    validate_iin(iin)
    kwargs['birth_date'] = birth_date_from_iin(iin)
    return Staff.objects.create(**kwargs)


def update_staff(*, staff_id, **kwargs):
    staff = get_staff(staff_id=staff_id)
    staff.update(**kwargs)
    return staff


def delete_staff(*, staff_id):
    staff = get_staff(staff_id=staff_id)
    staff.delete()


def validate_iin(iin):
    if not iin:
        raise exceptions.ValidationError('IIN cannot be null')
    # TODO: Normal Validation


def birth_date_from_iin(iin):
    century = iin[7]
    if century in ['1', '2']:
        year = 1800

    elif century in ['3', '4']:
        year = 1900
    else:
        year = 2000

    year += int(iin[:2])
    month = int(iin[2:4])
    day = int(iin[4:6])
    return date(year=year, month=month, day=day)
