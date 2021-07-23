import factory

from apps.restaurants.models import Restaurant


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker('company')
    address = factory.Faker('address')
    description = factory.Faker('sentence')
    date_opened = factory.Faker('past_date')