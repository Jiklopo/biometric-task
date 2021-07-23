from django.core.exceptions import ValidationError
from ..models import Restaurant
from .fixtures import create_restaurant
import datetime
import pytest


def test_date_opened(create_restaurant):
    future = datetime.date.today() + datetime.timedelta(days=1)
    restaurant = create_restaurant
    restaurant.date_opened = future
    with pytest.raises(ValidationError):
        restaurant.full_clean()
