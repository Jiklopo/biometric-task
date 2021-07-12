from django.contrib import admin
from .models import Staff, Restaurant, Pizza, Person

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Staff)
admin.site.register(Pizza)
admin.site.register(Person)
