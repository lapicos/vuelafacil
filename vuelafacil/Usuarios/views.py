from rest_framework import viewsets
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
from Usuarios.serializers import *

class UsuariosAPI(viewsets.ModelViewSet):
    serializer_class=UserSerial
    queryset=get_user_model().objects.all()

class PerfilesAPI(viewsets.ModelViewSet):
    serializer_class=PerfilSerial
    queryset=Perfil.objects.all()