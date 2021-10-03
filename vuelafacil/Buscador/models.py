from django.db import models
from Aeropuertos.models import Aeropuerto

class Buscador(models.Model):
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
    aerolinea=models.CharField(max_length=3)
          
    def __str__(self):
        return "Opción de ruta # "+ str(self.id_ruta) + str(self.aeropuerto_origen)+"-"+str(self.aeropuerto_destino)