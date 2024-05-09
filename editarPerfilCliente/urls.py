from django.urls import path
from . import views

urlpatterns = [
    path('editarPerfil/', views.registrar_cliente, name='editarPerfilCliente'),
]