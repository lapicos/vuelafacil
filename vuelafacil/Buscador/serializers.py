from rest_framework import serializers

from .models import *

class BuscadorSerial(serializers.ModelSerializer):
    class Meta:
        model = Buscador
        fields = '__all__'