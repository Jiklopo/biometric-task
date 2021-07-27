from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import serializers, status

from drf_yasg.utils import swagger_auto_schema

from .models import Restaurant
from .selectors import restaurants_list, get_restaurant
from .services import create_restaurant, update_restaurant, delete_restaurant


class RestaurantsListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantsListOutputSerializer'
            model = Restaurant
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='List Restaurants',
        responses={200: OutputSerializer()}
    )
    def get(self, request: Request):
        restaurants = restaurants_list()
        data = self.OutputSerializer(restaurants, many=True).data
        return Response(data)


class RestaurantCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        address = serializers.CharField(
            max_length=128,
            allow_blank=True,
            required=False
        )
        description = serializers.CharField(required=False)
        date_opened = serializers.DateField(required=False)

        class Meta:
            ref_name = 'RestaurantCreateInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantCreateOutputSerializer'
            model = Restaurant
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Create Restaurant',
        request_body=InputSerializer,
        responses={201: OutputSerializer()}
    )
    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        restaurant = create_restaurant(**serializer.validated_data)
        response_data = self.OutputSerializer(instance=restaurant).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class RestaurantUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128, required=False)
        description = serializers.CharField(required=False)
        rating = serializers.IntegerField()

        class Meta:
            ref_name = 'RestaurantUpdateInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'RestaurantUpdateOutputSerializer'
            model = Restaurant
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Update Restaurant',
        request_body=InputSerializer,
        responses={200: OutputSerializer()}
    )
    def post(self, request: Request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        restaurant = get_restaurant(restaurant_id=id)
        restaurant = update_restaurant(restaurant=restaurant, **serializer.validated_data)
        response_data = self.OutputSerializer(instance=restaurant).data
        return Response(data=response_data, status=status.HTTP_200_OK)


class RestaurantDeleteApi(APIView):
    @swagger_auto_schema(
        operation_description='Delete Restaurant',
        responses={204: ''}
    )
    def delete(self, request: Request, id):
        restaurant = get_restaurant(restaurant_id=id)
        delete_restaurant(restaurant=restaurant)
        return Response(status=status.HTTP_204_NO_CONTENT)
