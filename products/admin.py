from django.contrib import admin

from products.models import Item, BotType


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(BotType)
class BotAdmin(admin.ModelAdmin):
    pass