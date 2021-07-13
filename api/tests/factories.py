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

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda a: f'{a.first_name[0]}.{a.last_name}@biometric.kz'
    )
    gender = FuzzyChoice(Staff.GenderTextChoices.choices)
    job = FuzzyChoice(Staff.JobTextChoices.choices)
    birth_date = factory.Faker('date')
    date_joined = factory.Faker('date')

    @classmethod
    def create(cls, **kwargs):
        restaurant = Restaurant.objects.order_by('?').first()

        if not restaurant:
            restaurant = RestaurantFactory()

        instance = super().create(restaurant=restaurant, **kwargs)
        return instance


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    restaurant = factory.SubFactory(RestaurantFactory)
    name = factory.Faker('first_name')
    cheese = factory.Faker('last_name')
    pastry = FuzzyChoice(['thin', 'thick'])
    secret_ingredient = factory.Faker('name')