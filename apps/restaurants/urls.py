from django.urls import path
from .views import (
    RestaurantCreateApi,
    RestaurantUpdateApi,
    RestaurantDeleteApi,
    RestaurantsListApi
)

urlpatterns = [
    path('', RestaurantsListApi.as_view(), name='list'),
    path('create/', RestaurantCreateApi.as_view(), name='create'),
    path('update/', RestaurantUpdateApi.as_view(), name='update'),
    path('delete/', RestaurantDeleteApi.as_view(), name='delete'),
]
