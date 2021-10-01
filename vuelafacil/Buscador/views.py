from rest_framework import viewsets
import rest_framework
from rest_framework import response
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import *

class BuscadorAPI (viewsets.ViewSet):
    def list(self, request):
        busquedas = Buscador.objects.all()
        serializador = BuscadorSerial(busquedas, many=True)
        return Response(serializador.data)
