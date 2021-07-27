from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import serializers, status

from drf_yasg.utils import swagger_auto_schema

from .tasks import cook_pizzas
from apps.pizzas.models import Pizza
from apps.pizzas.selectors import list_pizzas, get_pizza
from apps.pizzas.services import create_pizza, update_pizza, delete_pizza
from apps.restaurants.selectors import get_restaurant


class PizzaListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaListOutputSerializer'
            model = Pizza
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='List Pizzas',
        responses={200: OutputSerializer()}
    )
    def get(self, request: Request):
        pizzas = list_pizzas()
        serializer = self.OutputSerializer(instance=pizzas, many=True)
        return Response(data=serializer.data)


class PizzaCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        restaurant = serializers.IntegerField()

        name = serializers.CharField(max_length=128)
        cheese = serializers.CharField(max_length=128, required=False)
        pastry = serializers.CharField(max_length=128, required=False)
        secret_ingredient = serializers.CharField(max_length=128, required=False)

        cooking_time = serializers.FloatField(required=False)

        class Meta:
            ref_name = 'PizzaInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaOutputSerializer'
            model = Pizza
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Create Pizza',
        request_body=InputSerializer,
        responses={201: OutputSerializer()}
    )
    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        restaurant = get_restaurant(restaurant_id=serializer.validated_data.pop('restaurant'))
        pizza = create_pizza(
            restaurant=restaurant,
            **serializer.validated_data
        )

        response_data = self.OutputSerializer(instance=pizza).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class PizzaUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        cheese = serializers.CharField(max_length=128, required=False)
        pastry = serializers.CharField(max_length=128, required=False)
        secret_ingredient = serializers.CharField(max_length=128, required=False)

        class Meta:
            ref_name = 'PizzaInputSerializer'

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaOutputSerializer'
            model = Pizza
            fields = '__all__'

    @swagger_auto_schema(
        operation_description='Update Pizza',
        request_body=InputSerializer,
        responses={200: OutputSerializer()}
    )
    def post(self, request: Request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pizza = get_pizza(pizza_id=id)
        pizza = update_pizza(pizza=pizza, **serializer.validated_data)

        response_data = self.OutputSerializer(instance=pizza).data
        return Response(data=response_data)


class PizzaDeleteApi(APIView):
    @swagger_auto_schema(
        operation_description='Delete Pizza',
        responses={204: ''}
    )
    def delete(self, request: Request, id):
        pizza = get_pizza(pizza_id=id)
        delete_pizza(pizza=pizza)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PizzaCookApi(APIView):
    class InputSerializer(serializers.Serializer):
        pizza_ids = serializers.ListField(child=serializers.IntegerField(), required=True)

        class Meta:
            ref_name = 'PizzaCookInputSerializer'
        
    @swagger_auto_schema(
        operation_description='Cook Pizzas by ID',
        request_body=InputSerializer
    )
    def post(self, request: Request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = cook_pizzas.delay(pizza_ids=serializer.validated_data.get('pizza_ids'))
        
        response = {
            'task_id': task.id,
            'task_status': task.status
        }
        return Response(data=response)
