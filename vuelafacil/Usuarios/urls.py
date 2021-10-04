from rest_framework import urlpatterns
from Usuarios.views import PerfilesAPI, UsuariosAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Usuarios.views import *

router=DefaultRouter()
router.register('usuarios', UsuariosAPI)
router.register('perfiles', PerfilesAPI)

urlpatterns=[
    path('crud/', include(router.urls)),
    path('logout', Logout.as_view()),
    path('login', Login.as_view())
]