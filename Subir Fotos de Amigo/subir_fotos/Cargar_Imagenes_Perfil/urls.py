from django.urls import path
from . import views

urlpatterns = [
    path('cargar_fotos_perfil/', views.cargar_fotos_perfil, name='cargar_fotos_perfil'),
    path('exito/', views.exito, name='exito'),
]