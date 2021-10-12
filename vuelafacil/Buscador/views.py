from django.views import View
from django.shortcuts import render, HttpResponse
from Aeropuertos.models import Aeropuerto
from Buscador.util.consultaAmadeus import *

def resultado(request):
    #answer=buscador.consultarAmadeus('BOG','CUC','2021-12-15','2021-12-16',1)
    answer=pd.read_excel('G:/Mi unidad/Capacitaciones/UIS - Desarrollo de software/Scripts/amadeus.xlsx') 
    index={'id':answer['id'], 
    'durationdeparture':answer['departureDuration'],
    'stopdeparture':answer['departureStop'],
    'departureat':answer['departureAt'],
    'arrivalat':answer['arrivalAt'],
    'departureorigin': answer['departureOriginIata'],
    'departuredestination':answer['departureDestinationIata'],
    'durationreturn':answer['returnDuration'],
    'stopreturn':answer['returnStop'],
    'returnat':answer['returnAt'],
    'arrivalreturnerAt':answer['arrivalreturnerAt'],
    'returnorigin':answer['returnOriginIataCode'],
    'returndestination':answer['returnDestinationIata'],
    'seats':answer['seats'],
    'oneway':answer['oneWay'],
    'pricebase':answer['priceBase'],
    'pricetotal':answer['priceTotal'],
    'airline':answer['airline'],
    }
    
    return render (request, "Buscador/search.html",index)