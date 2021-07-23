import factory

from apps.pizzas.models import Pizza


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    name = factory.Faker('word')
    cheese = factory.Faker('word')
    pastry = factory.Faker('word')
    secret_ingredient = factory.Faker('word')
