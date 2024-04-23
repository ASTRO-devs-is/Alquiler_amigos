from django.urls import path
from . import views

urlpatterns = [
    path('cuenta/<amigo_id>', views.visualizarPerfilAmigo, name="crearCuenta"), 
]