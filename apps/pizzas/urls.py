from django.urls import path

from apps.pizzas.views import PizzaListApi, PizzaCreateApi, PizzaUpdateApi, PizzaDeleteApi

urlpatterns = [
    path('', PizzaListApi.as_view(), name='list'),
    path('create/', PizzaCreateApi.as_view(), name='create'),
    path('update/', PizzaUpdateApi.as_view(), name='update'),
    path('delete/', PizzaDeleteApi.as_view(), name='delete'),
]
