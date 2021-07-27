from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404

from apps.pizzas.models import Pizza


def list_pizzas() -> QuerySet[Pizza]:
    return Pizza.objects.all()


def get_pizza(*, pizza_id) -> Pizza:
    q = Pizza.objects.all()
    return get_object_or_404(q, id=pizza_id)


def get_pizzas(**kwargs) -> QuerySet[Pizza]:
    return Pizza.objects.filter(**kwargs)
