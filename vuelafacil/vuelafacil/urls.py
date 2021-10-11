from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Buscador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeropuertos/api/', include('Aeropuertos.urls')),
    path('users/api/', include('Usuarios.urls')),
    #path('buscador/api/', include('Buscador.urls')),
    path('checkout/api', include('Checkout.urls')),
    path('search/', views.resultado, name="search")

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

