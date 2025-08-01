from rest_framework import serializers
from .models import ClientTovar

class ClientTovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTovar
        fields = ['id', 'name_prep', 'ean13']
