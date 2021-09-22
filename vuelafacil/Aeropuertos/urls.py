from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('aeropuerto', AeropuertosAPI, basename="aeropuerto"),
router.register('ruta', AeropuertosAPI, basename="ruta")

urlpatterns = [
    path('crud/', include(router.urls))
]