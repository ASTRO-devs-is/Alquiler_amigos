from django.urls import path
from . import views

urlpatterns = [
    path('cuenta/', views.visualizarPerfilAmigo, name="crearCuenta"), 
]