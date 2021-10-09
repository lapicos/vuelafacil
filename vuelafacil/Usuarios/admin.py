from django.contrib import admin

from Usuarios.models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombres', 'apellidos', 'pais', 'ciudad',)
    search_fields = ('usuario', 'nombres',)
    list_filter = ('usuario', 'nombres', 'apellidos', 'pais', 'ciudad',)