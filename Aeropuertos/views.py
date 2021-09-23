from rest_framework import viewsets
import rest_framework
from rest_framework import response
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import *

class AeropuertosAPI (viewsets.ViewSet):
    def list(self, request):
        aeropuertos = Aeropuerto.objects.all()
        serializador = AeropuertoSerial(aeropuertos, many=True)
        return Response(serializador.data)

class RutasApi(viewsets.ViewSet):
    def list(self, request):
        rutas = Ruta.objects.all()
        serializador = RutaSerial(rutas, many=True)
        return Response(serializador.data)

