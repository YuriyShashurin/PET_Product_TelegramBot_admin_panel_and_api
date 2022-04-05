from django.shortcuts import render
from products.models import Item
from rest_framework.viewsets import ModelViewSet
from API.serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
