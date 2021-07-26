import pytest

from apps.pizzas.factories import PizzaFactory


@pytest.fixture
def create_pizza(db):
    return PizzaFactory()


@pytest.fixture
def build_pizza(db):
    pizza = PizzaFactory.build()
    pizza_dict = pizza.__dict__
    pizza_dict.pop('__state')
    return pizza_dict
