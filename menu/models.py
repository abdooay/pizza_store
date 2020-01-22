from django.db import models
import uuid

PIZZA_SIZE = (
    ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'))

PIZZA_SIZE_DIC = dict(PIZZA_SIZE)


# Create your models here.
class Pizza(models.Model):
    # TODO: Common attributes can be moved to Abstract base class
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    available_size = models.CharField

    def __str__(self):
        return self.name


class PizzaPrice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pizza = models.ForeignKey(to=Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=PIZZA_SIZE)
    price = models.IntegerField()

    class Meta:
        unique_together = ['pizza', 'size']

    def __str__(self):
        # TODO: Lazy Loading Issue N+1
        return f"{self.pizza.name} / {PIZZA_SIZE_DIC[self.size]} / {self.price}"
