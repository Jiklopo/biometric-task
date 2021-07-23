from rest_framework import exceptions

from apps.pizzas.models import Pizza
from apps.pizzas.selectors import get_pizza
from apps.utils import update_model


def create_pizza(**kwargs):
    return Pizza.objects.create(**kwargs)


def update_pizza(*, pizza_id: int, **kwargs):
    pizza = get_pizza(pizza_id=pizza_id)
    return update_model(model=pizza, **kwargs)


def delete_pizza(*, pizza_id: int):
    pizza = get_pizza(pizza_id=pizza_id)
    pizza.delete()
