from django.shortcuts import render
from products.models import Item, BotType
from rest_framework.viewsets import ModelViewSet
from API.serializers import ItemSerializer, BotTypeSerializer



class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BotTypeViewSet(ModelViewSet):
    queryset = BotType.objects.all()
    serializer_class = BotTypeSerializer
