from ..models import Restaurant, Staff, Pizza
from factory.fuzzy import FuzzyChoice
import factory


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker('company')
    address = factory.Faker('address')


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    restaurant = factory.SubFactory(RestaurantFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda a: f'{a.first_name[0]}.{a.last_name}@biometric.kz'
    )
    gender = FuzzyChoice(Staff.GenderTextChoices.choices)
    job = FuzzyChoice(Staff.JobTextChoices.choices)
    birth_date = factory.Faker('date')
    date_joined = factory.Faker('date')


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    restaurant = factory.SubFactory(RestaurantFactory)
    name = factory.Faker('first_name')
    cheese = factory.Faker('last_name')
    pastry = FuzzyChoice(['thin', 'thick'])
    secret_ingredient = factory.Faker('name')