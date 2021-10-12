import pandas as pd 
import amadeus
from amadeus import Client , ResponseError
from Buscador.util.euroapeso import convertir_euros_a_pesos

class buscador:
    originLocationCode=""
    destinationLocationCode=""
    departureDate=""
    returnDate=""
    adults=1

    def __init__(self, originLocationCode, destinationLocationCode, departureDate,returnDate,adults):
        self.originLocationCode=originLocationCode
        self.destinationLocationCode=destinationLocationCode
        self.departureDate=departureDate
        self.returnDate=returnDate
        self.adults=adults

    def consultarAmadeus(originLocationCode, destinationLocationCode, departureDate,returnDate,adults): 
        amadeus = Client(
        client_id='k13qixwlNUmuh0Sqlc8o6l5G3CnB9QbT',
        client_secret='E58AkZ71R2TxWhDq'
        )
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=originLocationCode, 
                destinationLocationCode=destinationLocationCode,
                departureDate=departureDate, 
                returnDate=returnDate, 
                adults=1)
        except ResponseError as error:
            raise error
        respuesta=response.result
        
        data=pd.DataFrame()
#Genera DF con las opciones de vuelo disponible - pk=id
        for id in range (0,len(respuesta['data'])):
            data.loc[id,'id']=respuesta['data'][id]['id']
            data.loc[id,'departureDuration']=respuesta['data'][id]['itineraries'][0]['duration']
            departureStop=len(respuesta['data'][id]['itineraries'][0]['segments'])-1
            data.loc[id, 'departureStop']= departureStop
            data.loc[id,'departureAt']=respuesta['data'][id]['itineraries'][0]['segments'][0]['departure']['at'] 
            data.loc[id,'arrivalAt']=respuesta['data'][id]['itineraries'][0]['segments'][0]['arrival']['at'] 
            data.loc[id,'departureOriginIata']=respuesta['data'][id]['itineraries'][0]['segments'][0]['departure']['iataCode']
            data.loc[id,'departureDestinationIata']=respuesta['data'][id]['itineraries'][0]['segments'][departureStop]['arrival']['iataCode']  
            
            data.loc[id,'returnDuration']=respuesta['data'][id]['itineraries'][1]['duration']
            returnStop=len(respuesta['data'][id]['itineraries'][1]['segments'])-1
            data.loc[id, 'returnStop']= returnStop        
            data.loc[id,'returnAt']=respuesta['data'][id]['itineraries'][1]['segments'][0]['departure']['at'] 
            data.loc[id,'arrivalreturnerAt']=respuesta['data'][id]['itineraries'][1]['segments'][0]['arrival']['at'] 
            data.loc[id,'returnOriginIataCode']=respuesta['data'][id]['itineraries'][1]['segments'][0]['departure']['iataCode'] 
            data.loc[id,'returnDestinationIata']=respuesta['data'][id]['itineraries'][1]['segments'][returnStop]['arrival']['iataCode']  
            
            data.loc[id,'seats']=respuesta['data'][id]['numberOfBookableSeats']
            data.loc[id,'oneWay']=respuesta['data'][id]['oneWay']
            
            data.loc[id,'priceBase']=respuesta['data'][id]['price']['base']
            data.loc[id,'priceTotal']=respuesta['data'][id]['price']['total']
            
            data.loc[id,'airline']=respuesta['data'][id]['validatingAirlineCodes']

        data["priceBase"] = data.priceBase.astype(float)
        data["priceTotal"] = data.priceTotal.astype(float)

        data["priceBase"]=round(convertir_euros_a_pesos(data["priceBase"]),0)
        data["priceTotal"]=round(convertir_euros_a_pesos(data["priceTotal"]),0)
        return data
