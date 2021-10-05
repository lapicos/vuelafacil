from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets

from Checkout.serializers import *

class VoucherAPI(viewsets.ModelViewSet):
    serializer_class = VoucherSerial
    queryset = Voucher.objects.all()


class PagoAPI(viewsets.ModelViewSet):
    serializer_class = PagoSerial
    queryset = Pago.objects.all()


class MensajeAPI(viewsets.ModelViewSet):
    serializer_class = PagoSerial
    queryset = Mensaje.objects.all()
