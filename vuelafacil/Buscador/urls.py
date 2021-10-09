from os import name
from django.urls import path, include

from Buscador.views import *

urlpatterns = [
    path('', LandingPage.as_view(), name="landing")
]
