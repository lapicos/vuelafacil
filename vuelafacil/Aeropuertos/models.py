from django.db import models

class Aeropuerto(models.Model):
    oaci = models.CharField(max_length=4, primary_key=True)
    iata = models.CharField(max_length=3)
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    pais =  models.CharField(max_length=200)
    grados_longitud = models.FloatField(default=0)
    grados_latitud = models.FloatField(default=0)
    altitud = models.IntegerField(default=0)

    def __str__(self):
        return  self.iata + "," + self.nombre + "," + self.ciudad 
    
    def totalAeropuertos(self):
        aeropuertos = Aeropuerto.objects.all()
        return len(aeropuertos)

class Ruta(models.Model):
    origen = models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')
    destino = models.ForeignKey(Aeropuerto, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.origen.iata + "-" + self.destino
    
    def totalRutas(self):
        rutas = Ruta.objects.all()
        return len(rutas)