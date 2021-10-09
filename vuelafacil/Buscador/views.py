from django.views import View
from django.shortcuts import render, HttpResponse

from Aeropuertos.serializers import *

class LandingPage(View):
    template = 'index.html'
    #request => petición de usuario. Métodos de petición => GET, POST, PUT, PATCH y DELETE -> APIView
    def get(self, request):
        aeropuertos = Aeropuerto.objects.all()
        ciudades = []
        for puerto in aeropuertos:
            ciudades.append(puerto.ciudad)
        print(ciudades)
        return render(request, self.template, {'ciudades':ciudades})
    
    def post(self, request):
        return HttpResponse("Entra")
