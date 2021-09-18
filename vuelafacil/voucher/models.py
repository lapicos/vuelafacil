from django.db import models

class Voucher(models.Model):
    id_vuelo=models.IntegerField()
    nombre_pasajero=models.CharField(max_length=50)
    apellido_pasajero=models.CharField(max_length=50)
    fecha_nacimiento_pasajero=models.DateField()
    telefono_pasajero=models.CharField(max_length=10)
    email_pasajero=models.CharField(max_length=80)

    def __str__(self):
        return "Pasajero " +self.nombre_pasajero

def calcularValorTotal(self):
    pass

    
