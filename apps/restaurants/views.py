from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from rest_framework import serializers, exceptions, status

from .models import Restaurant, Pizza, Staff
from .selectors import restaurants_list
from .serializers import (
    RestaurantSerializer,
    PizzaSerializer,
    StaffSerializer
)
from ..services import create_restaurant, update_restaurant, delete_restaurant


class RestaurantsListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantsListOutputSerializer'
            model = Restaurant
            fields = '__all__'

    def get(self, request: Request):
        restaurants = restaurants_list()
        data = self.OutputSerializer(restaurants, many=True).data
        return Response(data)


class RestaurantCreateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantCreateInputSerializer'
            model = Restaurant
            fields = [
                'name',
                'address',
                'description',
                'date_opened'
            ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantCreateOutputSerializer'
            model = Restaurant
            fields = '__all__'

    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = create_restaurant(**serializer.validated_data)
        response = self.OutputSerializer(instance=restaurant)
        return Response(data=response.data, status=status.HTTP_201_CREATED)


class RestaurantUpdateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantUpdateInputSerializer'
            model = Restaurant
            fields = '__all__'

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantUpdateOutputSerializer'
            model = Restaurant
            fields = ['id']

    def put(self, request: Request):
        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        r = update_restaurant(**serializer.validated_data)
        response_data = self.OutputSerializer(instance=r).data
        return Response(data=response_data, status=status.HTTP_200_OK)


class RestaurantDeleteApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantDeleteInputSerializer'
            model = Restaurant
            fields = ['id']

    def delete(self, request: Request):
        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        restaurant_id = serializer.validated_data.get('id')
        if not restaurant_id:
            raise exceptions.NotAcceptable
        delete_restaurant(restaurant_id=restaurant_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
