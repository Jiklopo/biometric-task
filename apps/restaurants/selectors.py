from apps.restaurants.models import Restaurant


def restaurants_list():
    return Restaurant.objects.all()
