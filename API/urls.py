from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r'products', views.ItemViewSet)
router.register(r'bots', views.BotTypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]


