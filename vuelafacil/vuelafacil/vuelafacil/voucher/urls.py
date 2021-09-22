from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from voucher.views import *

router=DefaultRouter()
router.register('voucher', VoucherAPI,)

urlpatterns=[
    path('crud/',include(router.urls))
]