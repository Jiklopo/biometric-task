from rest_framework import exceptions
from apps.restaurants.models import Restaurant
from apps.restaurants.selectors import get_restaurant
from apps.utils import update_model


def create_restaurant(**kwargs):
    restaurant = Restaurant(**kwargs)
    restaurant.save()
    return restaurant


def update_restaurant(*, restaurant_id, **kwargs):
    restaurant = get_restaurant(restaurant_id=restaurant_id)
    return update_model(model=restaurant, **kwargs)


def delete_restaurant(*, restaurant: Restaurant):
    restaurant.delete()
