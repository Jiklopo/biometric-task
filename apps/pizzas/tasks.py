import time
from apps.pizzas.selectors import get_pizza
from apps.taskapp.celery import celery_app


@celery_app.task
def cook_pizzas(*, pizza_ids: list[int] = None):
    if len(pizza_ids) > 0:
        pizza = get_pizza(pizza_id=pizza_ids.pop(0))
        if pizza.state != 'DONE':
            pizza.state = 'COOKING'
            pizza.save()
            time.sleep(pizza.cooking_time)
            pizza.state = 'DONE'
            pizza.save()
        return cook_pizzas.delay(pizza_ids=pizza_ids)