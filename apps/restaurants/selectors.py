from rest_framework.generics import get_object_or_404

from apps.restaurants.models import Restaurant


def get_restaurant(*, restaurant_id):
    q = Restaurant.objects.all()
    return get_object_or_404(q, id=restaurant_id)


def restaurants_list():
    return Restaurant.objects.all()
