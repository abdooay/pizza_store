from rest_framework import serializers
from .models import Pizza, PizzaType


class PizzaTypeSerializer(serializers.ModelSerializer):
    # price = serializers.IntegerField()

    class Meta:
        model = PizzaType
        fields = ['uuid', 'price', 'size']


class MenuSerializer(serializers.ModelSerializer):
    pizza_types = PizzaTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = ['id', 'uuid', 'name', 'description', 'pizza_types']
