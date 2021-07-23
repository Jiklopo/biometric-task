from apps.pizzas.models import Pizza


def list_pizzas():
    return Pizza.objects.all()