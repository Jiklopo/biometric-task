from .models import Restaurant, Pizza, Person
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from datetime import datetime


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address']


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            'id',
            'name',
            'cheese',
            'pastry',
            'secret_ingredient',
            'restaurant'
        ]


class PersonSerializer(ModelSerializer):
    def get_age(self, iin):
        century = iin[7]
        if century in ['1', '2']:
            year = 1800
        elif century in ['3', '4']:
            year = 1900
        else:
            year = 2000

        year += int(iin[:2])
        month = int(iin[2:4])
        day = int(iin[4:6])
        birth_date = datetime(year=year, month=month, day=day)
        return (datetime.today() - birth_date).days // 365.25

    def to_representation(self, instance):
        r = super().to_representation(instance)
        r['age'] = self.get_age(r['iin'])
        return r

    class Meta:
        model = Person
        fields = ['iin', 'age']
