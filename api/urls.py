from django.urls import path
from .views import (
    ListRestaurantsAPIView,
    RestaurantAPIView,
    ListPizzasAPIView,
    PizzaAPIView,
    ListStaffAPIView,
    StaffAPIView,
)

urlpatterns = [
    path('restaurants/', ListRestaurantsAPIView.as_view(), name='all-restaurants'),
    path('restaurants/<int:pk>/', RestaurantAPIView.as_view(), name='restaurant'),

    path('pizzas/', ListPizzasAPIView.as_view(), name='all-pizzas'),
    path('pizzas/<int:pk>/', PizzaAPIView.as_view(), name='pizza'),

    path('staff/', ListStaffAPIView.as_view(), name='all-staff'),
    path('staff/<int:pk>', StaffAPIView.as_view(), name='staff'),
]
