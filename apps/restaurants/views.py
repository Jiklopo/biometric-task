from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import serializers, status

from drf_yasg.utils import swagger_auto_schema

from .models import Restaurant
from .selectors import restaurants_list
from .services import create_restaurant, update_restaurant, delete_restaurant


class RestaurantsListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantsListOutputSerializer'
            model = Restaurant
            fields = '__all__'

    @swagger_auto_schema(operation_description='List Restaurants')
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

    @swagger_auto_schema(
        operation_description='Create Restaurant',
        request_body=InputSerializer
    )
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
            fields = [
                'name',
                'description',
                'rating'
            ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantUpdateOutputSerializer'
            model = Restaurant
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Update Restaurant',
        request_body=InputSerializer
    )
    def put(self, request: Request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = update_restaurant(restaurant_id=id, **serializer.validated_data)
        response_data = self.OutputSerializer(instance=r).data
        return Response(data=response_data, status=status.HTTP_200_OK)


class RestaurantDeleteApi(APIView):
    @swagger_auto_schema(operation_description='Delete Restaurant')
    def delete(self, request: Request, id):
        delete_restaurant(restaurant_id=id)
        return Response(status=status.HTTP_204_NO_CONTENT)
