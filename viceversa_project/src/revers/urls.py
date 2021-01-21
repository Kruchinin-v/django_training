from django.contrib import admin
from django.urls import path

from .views import revers

urlpatterns = [
    path('', revers, name='reverse'),
]