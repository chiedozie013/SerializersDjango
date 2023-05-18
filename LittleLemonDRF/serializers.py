from .models import MenuItem
from rest_framework import serializers

class MeniItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']