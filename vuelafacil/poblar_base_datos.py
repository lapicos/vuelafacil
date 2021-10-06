#Metodo para poblar base de datos Aeropuertos
from numpy import NaN
import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','vuelafacil.settings')
django.setup()

from Aeropuertos.models import Aeropuerto

aeropuertos = pd.read_csv("./2.csv")
prueba_aeropuertos2 = aeropuertos[['IATA','IACO','NOMBRE', 'CIUDAD INGLES', 'CIUDAD ESPANOL', 'PAIS INGLES', 'PAIS ESPAÑOL', 'GRADOS LONGITUD', 'GRADOS LATITUD', 'ALTITUD']]
aeropuertos = prueba_aeropuertos2.dropna(axis=0, subset=['IATA'])
aeropuertos = aeropuertos.drop_duplicates(subset=['IATA'])

for indice, fila in aeropuertos.iterrows():
    Aeropuerto.objects.create(
        iata = fila['IATA'],
        iaco = fila["IACO"],
        nombre = fila['NOMBRE'],
        ciudad = fila['CIUDAD ESPANOL'],
        pais = fila['PAIS ESPAÑOL'],
        grados_longitud = fila['GRADOS LONGITUD'],
        grados_latitud = fila['GRADOS LATITUD'],
        altitud = fila['ALTITUD']
    )
