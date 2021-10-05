from numpy.lib.utils import info
import pandas as pd
from django.db import models
from django.db.models.deletion import SET_NULL
from pandas.core.algorithms import mode
#from Buscador.models import *
from Aeropuertos.models import *

class Voucher(models.Model):
    idTiquete = models.IntegerField(default=0)
    id_ruta=models.IntegerField()
    duracion=models.CharField(max_length=20)
    disponibilidad=models.IntegerField(default=0)
    fecha_salida=models.CharField(max_length=50)
    fecha_llegada=models.CharField(max_length=50)
    aeropuerto_origen=models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    aeropuerto_destino=models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    paradas=models.IntegerField(default=0)
    oneway=models.BooleanField(default=False)
    precio_base=models.FloatField()
    precio_total=models.FloatField()
    aerolinea = models.CharField(max_length=200)
    idUsuario = models.CharField(max_length=200)
    mombreUsuario = models.CharField(max_length=200)
    apellidoUsuario= models.CharField(max_length=200)
    nVuelo= models.CharField(max_length=200)
    nPasajeros = models.CharField(max_length=200)
    
    def __str__(self):
        return self.idTiquete

    def calcularCargos(self):
        cargos = self.precio_total - self.precio_base
        return cargos

    def infoRuta(self):
        inforuta = (self.oneway, self.fecha_salida, self.aeropuerto_origen, self.aeropuerto_destino, self.paradas, self.duracion, 
                self.aerolinea, self.nVuelo, self.nPasajeros)
        return inforuta

    def infoCobro(self):
        infopago = (self.nPasajeros, self.precio_total, self.precio_base, self.calcularCargos())
        return infopago

class Pago(models.Model):
    idPago = models.IntegerField(default=0)
    fechaCompra = models.DateTimeField()
    estadoCompra = models.BooleanField()
    idTiquete = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    def __str__(self):
        return self.estadoCompra

    def infoPago(self):
        infoPago = (self.idPago, self.fechaCompra, self.estadoCompra, self.idTiquete)
        return infoPago


class Mensaje(models.Model):

    infopago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    inforuta = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    def __str__(self):
        return self.infopago

    def enviarMensaje(self):
        return 'Gracias por comprar con nosotros! tu itinerario en informacion de pago son:'
        + self.infopago.infoPago() + ' ' + self.inforuta.infoRuta()








