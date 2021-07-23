from rest_framework import exceptions

from apps.pizzas.models import Pizza


def create_pizza(**kwargs):
    return Pizza.objects.create(**kwargs)


def update_pizza(*, pizza_id: int, **kwargs):
    try:
        pizza = Pizza.objects.get(id=pizza_id)
        pizza.update(**kwargs)
        return pizza
    except Pizza.DoesNotExist:
        raise exceptions.NotFound


def delete_pizza(*, pizza_id: int):
    try:
        Pizza.objects.get(id=pizza_id).delete()
    except Pizza.DoesNotExist:
        raise exceptions.NotFound
