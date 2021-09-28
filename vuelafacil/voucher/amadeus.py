from amadeus import Client , ResponseError
from amadeus import Location


#Consulta a la API Amadeus para extraer los datos reales de vuelos
#Autenticacion
amadeus = Client(
        client_id='jmoHqSjWfqG1c48FiYzfVS26wohH8Am7',
        client_secret='Anbp8Ek1ZW2ZPsHq'
    )

def datosIda(origen, destino, fecha_ida, adultos):

    try:
        '''
        búsqueda de ofertas de vuelos de compras ida
        '''
        response = amadeus.shopping.flight_offers_search.get(originLocationCode=origen, destinationLocationCode=destino, departureDate=fecha_ida, adults=adultos)
        return(response.data)
    except ResponseError as error:
        raise error

def datosIdaVuelta(origen, destino, fecha_ida, fecha_vuelta, adultos):

    try:
        '''
        búsqueda de ofertas de vuelos de compras ida y vuelta
        '''
        response = amadeus.shopping.flight_offers_search.get(originLocationCode=origen, destinationLocationCode=destino, departureDate=fecha_ida, returnDate=fecha_vuelta, adults=adultos)
        return(response.data)
    except ResponseError as error:
        raise error