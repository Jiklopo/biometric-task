import pytest
from rest_framework.test import APIClient

from apps.pizzas.tests.fixtures import *
from apps.restaurants.tests.fixtures import *
from apps.staff.tests.fixtures import *


@pytest.fixture
def api_client():
    return APIClient()
