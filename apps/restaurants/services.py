from rest_framework import exceptions
from apps.restaurants.models import Restaurant


def create_restaurant(**kwargs):
    return Restaurant.objects.create(**kwargs)


def update_restaurant(**kwargs):
    if 'id' not in kwargs:
        raise exceptions.NotFound

    try:
        r = Restaurant.objects.get(id=kwargs['id'])
        r.update(**kwargs)
    except Restaurant.DoesNotExist:
        raise exceptions.NotFound
    return r


def delete_restaurant(*, restaurant_id: int):
    try:
        Restaurant.objects.get(id=restaurant_id).delete()
    except Restaurant.DoesNotExist:
        raise exceptions.NotFound
