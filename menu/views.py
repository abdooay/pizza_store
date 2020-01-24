from django.shortcuts import render
from rest_framework import viewsets
from .models import Pizza
from .serializers import MenuSerializer


# Create your views here.
class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = MenuSerializer
