from django.urls import path

from apps.taskapp.views import TaskViewApi

urlpatterns = [
    path('<str:task_id>/', TaskViewApi.as_view(), name='view-task')
]
