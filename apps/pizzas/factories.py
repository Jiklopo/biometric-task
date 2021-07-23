import factory

from apps.pizzas.models import Pizza
from apps.restaurants.factories import RestaurantFactory
from apps.restaurants.models import Restaurant


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    name = factory.Faker('word')
    cheese = factory.Faker('word')
    pastry = factory.Faker('word')
    secret_ingredient = factory.Faker('word')

    @classmethod
    def create(cls, **kwargs):
        restaurant = Restaurant.objects.order_by('?').first()

        if not restaurant:
            restaurant = RestaurantFactory()

        return super().create(restaurant=restaurant, **kwargs)
