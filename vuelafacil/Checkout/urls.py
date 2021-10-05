
from django.db import router
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from Checkout.views import *


router = DefaultRouter()
router.register('voucher', VoucherAPI)
router.register('pago', PagoAPI)
router.register('mensaje', MensajeAPI)

urlpatterns = [

    path('crud/',include(router.urls))
]
