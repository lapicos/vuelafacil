from voucher.models import Voucher
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers

from voucher.models import *

class VoucherSerial(ModelSerializer):
    class Meta:
        model=Voucher
        fields='__all__'
