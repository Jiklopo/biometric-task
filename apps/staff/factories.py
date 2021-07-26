from random import choice

import factory

from apps.restaurants.factories import RestaurantFactory
from apps.restaurants.models import Restaurant
from apps.staff import GenderChoices, JobChoices
from apps.staff.models import Staff
from apps.staff.services import generate_iin


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    iin = generate_iin()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    gender = factory.LazyAttribute(lambda s: choice(GenderChoices.choices)[0])
    job = factory.LazyAttribute(lambda s: choice(JobChoices.choices)[0])
    email = factory.Faker('email')
    date_joined = factory.Faker('past_date')

    @classmethod
    def build(cls, **kwargs):
        restaurant = Restaurant.objects.order_by('?').first()

        if not restaurant:
            restaurant = RestaurantFactory()

        return super().build(restaurant=restaurant, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        restaurant = Restaurant.objects.order_by('?').first()

        if not restaurant:
            restaurant = RestaurantFactory()

        return super().create(restaurant=restaurant, **kwargs)
