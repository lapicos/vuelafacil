from rest_framework import serializers

from .models import *

class BucadorSerial(serializers.ModelSerializer):
    class Meta:
        model = Buscador
        fields = '__all__'