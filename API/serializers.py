from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Item, BotType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class BotTypeSerializer(serializers.ModelSerializer):
    allowed_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = BotType
        fields = ['id', 'name', 'description', 'owner', 'allowed_users']


class ItemSerializer(serializers.ModelSerializer):
    bot = BotTypeSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'article', 'price', 'country', 'color', 'date_created', 'image', 'bot']


