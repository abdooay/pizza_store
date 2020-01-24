from django.contrib import admin
from .models import Pizza, PizzaType

# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaType)
