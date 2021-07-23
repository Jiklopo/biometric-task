from rest_framework import exceptions
from apps.restaurants.models import Restaurant
from apps.restaurants.selectors import get_restaurant
from apps.utils import update_model


def create_restaurant(**kwargs):
    return Restaurant.objects.create(**kwargs)


def update_restaurant(*, restaurant_id, **kwargs):
    restaurant = get_restaurant(restaurant_id=restaurant_id)
    return update_model(model=restaurant, **kwargs)


def delete_restaurant(*, restaurant_id: int):
    try:
        Restaurant.objects.get(id=restaurant_id).delete()
    except Restaurant.DoesNotExist:
        raise exceptions.NotFound
