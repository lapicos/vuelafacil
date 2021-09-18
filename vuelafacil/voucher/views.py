from rest_framework import viewsets

from voucher.serializers import *

class VoucherAPI(viewsets.ModelViewSet):
    serializer_class=VoucherSerial
    queryset=Voucher.objects.all()