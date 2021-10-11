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

            data["priceBase"] = data.priceBase.astype(float)
            data["priceTotal"] = data.priceTotal.astype(float)

        for i in range(len(data['priceBase'])):
            data.loc[i,'priceBase'] =round(convertir_euros_a_pesos(data.loc[i,'priceBase']),0)
            data.loc[i,'priceTotal'] =round(convertir_euros_a_pesos(data.loc[i,'priceTotal']),0)

        return data