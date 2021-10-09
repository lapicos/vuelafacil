from django.contrib import admin
from .models import *

@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ('oaci', 'iata', 'nombre', 'ciudad',)
    search_fields = ('iata', 'nombre', 'ciudad',)
    list_filter = ('iata', 'nombre', 'ciudad',)
admin.site.register(Ruta)

