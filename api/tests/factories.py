from ..models import Restaurant, Staff
import factory


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker('company')
    address = factory.Faker('address')


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Staff'

    restaurant_id = 1
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda a: f'{a.first_name[0]}.{a.last_name}@biometric.kz'
    )
    gender = Staff.GenderTextChoices.choices[0]
    job = Staff.JobTextChoices.choices[0]
    birth_date = factory.Faker('date')
    date_joined = factory.Faker('date')
