from rest_framework import serializers
from .models import Prices

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ('date', 'origin_code', 'destination_code', 'price')