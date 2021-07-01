from .models import Restaurant, Pizza, Person
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import (
    RestaurantSerializer,
    PizzaSerializer,
    PersonSerializer,
)


class ListRestaurantsAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['id'])


class ListPizzasAPIView(generics.ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzaAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['id'])


class CreatePersonAPIView(generics.CreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class RetrievePersonAPIView(generics.RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, iin=self.kwargs['iin'])
