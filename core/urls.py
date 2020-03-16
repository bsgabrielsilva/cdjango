from django.urls import path

from .views import *

urlpatterns = [
    path('', home_core, name="home_core")
]