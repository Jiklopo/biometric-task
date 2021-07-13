from .models import Restaurant, Pizza, Staff
from rest_framework.serializers import ModelSerializer


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


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
