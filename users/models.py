from django.db import models


# TODO: can use abstractions
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=20)


class Captain(models.Model):
    name = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=20)
