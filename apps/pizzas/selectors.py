from rest_framework.generics import get_object_or_404

from apps.pizzas.models import Pizza


def list_pizzas():
    return Pizza.objects.all()


def get_pizza(*, pizza_id):
    q = Pizza.objects.all()
    return get_object_or_404(q, id=pizza_id)


def get_pizzas(**kwargs):
    return Pizza.objects.filter(**kwargs)
