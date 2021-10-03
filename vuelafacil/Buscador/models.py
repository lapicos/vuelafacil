from django.db import models
import pandas as pd 
import amadeus
from amadeus import Client , ResponseError
from Aeropuertos.models import Aeropuerto

class Buscador(models.Model):
    id_ruta=models.IntegerField()
    duracion=models.CharField(max_length=20)
    disponibilidad=models.IntegerField(default=0)
    fecha_salida=models.DateField(auto_now_add=True)
    fecha_llegada=models.DateField(auto_now_add=True)
    aeropuerto_origen=models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    aeropuerto_destino=models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    paradas=models.IntegerField(default=0)
    oneway=models.BooleanField(default=False)
    precio_base=models.FloatField()
    precio_total=models.FloatField()
    aerolinea=models.CharField(max_length=3)
          
    def __str__():
        return "Opción de ruta # "+ self.id_ruta
    
    def consultarAmadeus(self,origin, destination, departureDate, returnDate, adults): 
        amadeus = Client(
            client_id='jmoHqSjWfqG1c48FiYzfVS26wohH8Am7',
            client_secret='Anbp8Ek1ZW2ZPsHq'
        )
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode='BOG', 
                destinationLocationCode='SMR', 
                departureDate='2021-12-14', 
                returnDate='2021-12-20', 
                adults=1)
        except ResponseError as error:
            raise error
        respuesta=response.result
        #Proceso de conversión al DataFrame
        data=pd.DataFrame()
        for id in range (0,len(respuesta['data'])):
            data.loc[id,'id']=respuesta['data'][id]['id']
            data.loc[id,'departureDuration']=respuesta['data'][id]['itineraries'][0]['duration']
            departureStop=len(respuesta['data'][id]['itineraries'][0]['segments'])-1
            data.loc[id, 'departureStop']= departureStop
            data.loc[id,'departureAt']=respuesta['data'][id]['itineraries'][0]['segments'][0]['departure']['at']     
            data.loc[id,'departureOriginIata']=respuesta['data'][id]['itineraries'][0]['segments'][0]['departure']['iataCode']
            data.loc[id,'departureDestinationIata']=respuesta['data'][id]['itineraries'][0]['segments'][departureStop]['arrival']['iataCode']  
            
            data.loc[id,'returnDuration']=respuesta['data'][id]['itineraries'][1]['duration']
            returnStop=len(respuesta['data'][id]['itineraries'][1]['segments'])-1
            data.loc[id, 'returnStop']= returnStop        
            data.loc[id,'returnAt']=respuesta['data'][id]['itineraries'][1]['segments'][0]['departure']['at'] 
            data.loc[id,'returnOriginIataCode']=respuesta['data'][id]['itineraries'][1]['segments'][0]['departure']['iataCode'] 
            data.loc[id,'returnDestinationIata']=respuesta['data'][id]['itineraries'][1]['segments'][returnStop]['arrival']['iataCode']  
            
            data.loc[id,'seats']=respuesta['data'][id]['numberOfBookableSeats']
            data.loc[id,'oneWay']=respuesta['data'][id]['oneWay']
            
            data.loc[id,'priceBase']=respuesta['data'][id]['price']['base']
            data.loc[id,'priceTotal']=respuesta['data'][id]['price']['total']
            
            data.loc[id,'airline']=respuesta['data'][id]['validatingAirlineCodes']

        return data

