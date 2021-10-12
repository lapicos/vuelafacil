from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Buscador.views import resultado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeropuertos/api/', include('Aeropuertos.urls')),
    path('users/api/', include('Usuarios.urls')),
    path('checkout/api', include('Checkout.urls')),
    path('search/', resultado, name="search")

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

