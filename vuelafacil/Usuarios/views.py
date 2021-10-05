from rest_framework import viewsets, views
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model, login, logout
from Usuarios.serializers import *
from Usuarios.permissions import AccesoInfoPersonal
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

class UsuariosAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,AccesoInfoPersonal)
    serializer_class=UserSerial
    queryset=get_user_model().objects.all()

class PerfilesAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AccesoInfoPersonal)
  
    serializer_class=PerfilSerial
    queryset=Perfil.objects.all()

class Logout (views.APIView):
    def post(self, request):
        serializador=UserSerial(request.user)
        if not request.user.is_anonymous():
            logout(request)
            return Response("El usuario a echo logout")
        return Response(serializador.user)

class Login (views.APIView):
    def post(self,request):
        usuario=get_list_or_404(get_user_model(), username=request.data['username'])
        if usuario.check_password(request.data['password']):
            login(request,usuario)
            return Response("El usuario "+ usuario.username)
        return Response ({"Login": False})
