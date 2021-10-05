
from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeropuertos/api/', include('Aeropuertos.urls')),
    path('users/api/', include('Usuarios.urls')),
    #path('buscador/api/', include('Buscador.urls')),
    path('checkout/api', include('Checkout.urls'))

]
