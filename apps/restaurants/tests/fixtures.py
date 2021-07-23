from apps.restaurants.tests.factories import RestaurantFactory, StaffFactory
import pytest


@pytest.fixture
def create_restaurant(db):
    return RestaurantFactory()


@pytest.fixture
def create_staff(db):
    return StaffFactory()
