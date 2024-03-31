from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('cargarFotos', views.cargar_fotos_perfil, name="subir_foto"), 
]