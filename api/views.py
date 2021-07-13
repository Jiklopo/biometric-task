from .models import Restaurant, Pizza, Staff
from rest_framework import generics
from .serializers import (
    RestaurantSerializer,
    PizzaSerializer,
    StaffSerializer
)


class ListRestaurantsAPIView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class ListPizzasAPIView(generics.ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzaAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class ListStaffAPIView(generics.ListCreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
