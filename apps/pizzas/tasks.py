import time
from apps.pizzas import selectors
from apps.taskapp.celery import celery_app


@celery_app.task
def cook_pizza(*, pizza_id: int):
    pizza = selectors.get_pizza(pizza_id=pizza_id)
    if pizza.state == 'DONE':
        return

    time.sleep(pizza.cooking_time * 60)
    pizza.state = 'DONE'
    pizza.save()