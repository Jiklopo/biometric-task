from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from rest_framework import serializers, status

from apps.pizzas.models import Pizza
from apps.pizzas.selectors import list_pizzas
from apps.pizzas.services import create_pizza, update_pizza, delete_pizza


class PizzaListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaListOutputSerializer'
            model = Pizza
            fields = '__all__'

    def get(self, request: Request):
        pizzas = list_pizzas()
        serializer = self.OutputSerializer(instance=pizzas, many=True)
        return Response(data=serializer.data)


class PizzaCreateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaInputSerializer'
            model = Pizza
            fields = ['name', 'cheese', 'pastry', 'secret_ingredient']

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaOutputSerializer'
            model = Pizza
            fields = '__all__'

    def post(self, request: Request):
        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        pizza = create_pizza(**serializer.validated_data)
        response_data = self.OutputSerializer(instance=pizza)
        return Response(data=response_data, status=status.HTTP_201_CREATED)


class PizzaUpdateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaInputSerializer'
            model = Pizza
            fields = ['id', 'secret_ingredient']

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaOutputSerializer'
            model = Pizza
            fields = ['id']

    def put(self, request: Request):
        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        pizza_id = serializer.validated_data.pop('id')
        pizza = update_pizza(pizza_id=pizza_id, **serializer.validated_data)
        response_data = self.OutputSerializer(instance=pizza).data
        return Response(data=response_data)


class PizzaDeleteApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            ref_name = 'PizzaDeleteInputSerializer'
            model = Pizza
            fields = ['id']

    def delete(self, request):
        serializer = self.InputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        pizza_id = serializer.validated_data.get('id')
        delete_pizza(pizza_id=pizza_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
