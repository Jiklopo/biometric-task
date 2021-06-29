from django.urls import path
from .views import (
    ListRestaurantsAPIView,
    RestaurantAPIView,
    ListPizzasAPIView,
    PizzaAPIView,
    CreatePersonAPIView,
    RetrievePersonAPIView
)

urlpatterns = [
    path('restaurants/', ListRestaurantsAPIView.as_view(), name='all-restaurants'),
    path('restaurants/<int:id>/', RestaurantAPIView.as_view(), name='restaurant'),

    path('pizzas/', ListPizzasAPIView.as_view(), name='all-pizzas'),
    path('pizzas/<int:id>/', PizzaAPIView.as_view(), name='pizza'),

    path('person/', CreatePersonAPIView.as_view(), name='create-person'),
    path('person/<iin>/', RetrievePersonAPIView.as_view(), name='get-person')
]