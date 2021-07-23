from random import choice

import factory

from apps.restaurants.factories import RestaurantFactory
from apps.restaurants.models import Restaurant
from apps.staff import GenderTextChoices, JobTextChoices
from apps.staff.models import Staff
from apps.staff.services import generate_iin


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    iin = generate_iin()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    gender = factory.LazyAttribute(lambda s: choice(GenderTextChoices.choices)[0])
    job = factory.LazyAttribute(lambda s: choice(JobTextChoices.choices)[0])
    email = factory.Faker('email')
    date_joined = factory.Faker('past_date')

    @classmethod
    def create(cls, **kwargs):
        restaurant = Restaurant.objects.order_by('?').first()

        if not restaurant:
            restaurant = RestaurantFactory()

        return super().create(restaurant=restaurant, **kwargs)
