from rest_framework import serializers
from products.models import Item, BotType


class BotTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotType
        fields = ['id', 'name', 'description']


class ItemSerializer(serializers.ModelSerializer):
    bot = BotTypeSerializer(read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'article', 'price', 'country', 'color', 'date_created', 'image', 'bot']


