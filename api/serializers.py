from .models import Restaurant, Pizza, Person
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from datetime import datetime


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'address',
            'description',
            'date_opened',
            'rating'
        ]


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
    class Meta:
        model = Person
        fields = ['iin', 'age']
