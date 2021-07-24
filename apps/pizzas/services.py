from apps.pizzas.models import Pizza
from apps.restaurants.models import Restaurant
from apps.utils import update_model


def create_pizza(*, restaurant: Restaurant, **kwargs):
    pizza = Pizza(restaurant=restaurant, **kwargs)
    pizza.save()
    return pizza


def update_pizza(*, pizza: Pizza, **kwargs):
    return update_model(model=pizza, **kwargs)


def delete_pizza(*, pizza: Pizza):
    pizza.delete()
