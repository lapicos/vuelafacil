from django.contrib import admin

from .models import *

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('idTiquete', 'id_ruta', 'idUsuario', 'mombreUsuario', 'apellidoUsuario', 'nVuelo',)
    search_fields = ('idTiquete', 'idUsuario', 'mombreUsuario',)
    list_filter = ('idTiquete', 'idUsuario', 'mombreUsuario',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('idPago', 'fechaCompra', 'estadoCompra', 'idTiquete',)
    search_fields = ('idPago', 'idTiquete',)
    list_filter = ('idPago', 'idTiquete',)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('infopago', 'inforuta',)
    search_fields = ('infopago', 'inforuta',)
    list_filter = ('infopago', 'inforuta',)

