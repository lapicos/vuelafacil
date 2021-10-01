from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('buscador', BuscadorAPI, basename="buscador"),
urlpatterns = [
    path('crud/', include(router.urls))
]