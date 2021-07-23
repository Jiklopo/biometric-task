from django.urls import path

from apps.staff.views import (
    StaffListApi,
    StaffCreateApi,
    StaffDeleteApi,
    StaffUpdateApi
)

urlpatterns = [
    path('', StaffListApi.as_view(), name='list'),
    path('create/', StaffCreateApi.as_view(), name='create'),
    path('<str:iin>/update/', StaffUpdateApi.as_view(), name='update'),
    path('<str:iin>/delete/', StaffDeleteApi.as_view(), name='delete'),
]
