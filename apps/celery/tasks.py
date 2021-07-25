from celery import Celery

app = Celery('tasks', broker='amqp://localhost:5672')


@app.task
def add(x, y):
    return x + y
