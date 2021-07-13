from django.contrib import admin
from .models import Staff, Restaurant, Pizza

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Staff)
admin.site.register(Pizza)
