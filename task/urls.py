from django.urls import path, re_path, include
from .views import PriceList
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/price', PriceList, basename='price')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
