from django.urls import path
from .views import (
    ListRestaurantsAPIView,
    RestaurantAPIView,
    ListPizzasAPIView,
    PizzaAPIView
)

urlpatterns = [
    path('restaurants/', ListRestaurantsAPIView.as_view(), name='all-restaurants'),
    path('restaurants/<int:id>/', RestaurantAPIView.as_view(), name='restaurant'),
    path('pizzas/', ListPizzasAPIView.as_view(), name='all-pizzas'),
    path('pizzas/<int:id>/', PizzaAPIView.as_view(), name='pizza')
]
