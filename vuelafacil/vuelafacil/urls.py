from voucher.models import Voucher
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('voucher/api/',include('voucher.urls'))
]
