from rest_framework import exceptions
from faker import Faker
from random import randint
from datetime import date

from apps.staff.models import Staff
from apps.staff.selectors import get_staff
from apps.utils import update_model


def create_staff(**kwargs):
    iin = kwargs.get('iin')
    validate_iin(iin)
    kwargs['birth_date'] = birth_date_from_iin(iin)
    return Staff.objects.create(**kwargs)


def update_staff(*, staff_id, **kwargs):
    staff = get_staff(staff_id=staff_id)
    return update_model(model=staff, **kwargs)


def delete_staff(*, staff_id):
    staff = get_staff(staff_id=staff_id)
    staff.delete()


def generate_iin() -> str:
    faker = Faker()
    date = ''.join(faker.date()[2:].split('-'))
    century = randint(3, 6)
    rand = faker.bothify('%' * 4)

    iin = f'{date}{century}{rand}'

    twelve_one = str(sum(int(iin[i]) * (i + 1) for i in range(11)) % 11)
    twelve_two = sum(int(iin[i + 1]) * i for i in range(1, 10))
    twelve_two_expr = 10 * int(iin[0]) + 11 * int(iin[1])
    twelve_two_total = str((twelve_two + twelve_two_expr) % 11)

    if int(twelve_one) != 10:
        iin += twelve_one
        return iin

    if int(twelve_two_total) != 10:
        iin += twelve_two_total
        return iin


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
