from .models import Restaurant, Pizza
from rest_framework.serializers import ModelSerializer


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
