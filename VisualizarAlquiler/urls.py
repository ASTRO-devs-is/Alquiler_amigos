from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizarAlquiler, name='visualizarAlquiler'),
]