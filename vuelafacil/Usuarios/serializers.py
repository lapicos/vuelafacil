from rest_framework import serializers
from django.contrib.auth import get_user_model
from Usuarios.models import *

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields='__all__'

class PerfilSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Perfil
        fields='__all__'