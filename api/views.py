from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer
from Shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

