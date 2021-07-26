from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.taskapp.celery import celery_app


class TaskViewApi(APIView):
    def get(self, request: Request, task_id):
        task = celery_app.AsyncResult(task_id)
        response_data = {
            'task_id': task.id,
            'task_status': task.status
        }

        if task.status == 'SUCCESS':
            response_data['result'] = 'Your pizza is ready'

        return Response(data=response_data)
