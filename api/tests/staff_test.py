from django.core.exceptions import ValidationError
from .fixtures import create_staff
import pytest
import datetime as dt


def test_email(create_staff):
    staff = create_staff
    staff.email = 'bad_really'
    with pytest.raises(ValidationError):
        staff.full_clean()


def test_birth_date(create_staff):
    staff = create_staff
    staff.birth_date = dt.date.today() + dt.timedelta(days=1)
    with pytest.raises(ValidationError):
        staff.full_clean()


def test_date_joined(create_staff):
    staff = create_staff
    staff.date_joined = dt.date.today() + dt.timedelta(days=1)
    with pytest.raises(ValidationError):
        staff.full_clean()
