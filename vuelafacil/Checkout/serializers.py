
from django.db.models import fields
from Checkout.models import Mensaje, Pago, Voucher
from rest_framework import serializers
from Checkout import *

class VoucherSerial(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class PagoSerial(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class MensajeSerial(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'



