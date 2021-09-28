from rest_framework import serializers

from .models import *

class AeropuertoSerial(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = '__all__'

class RutaSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'