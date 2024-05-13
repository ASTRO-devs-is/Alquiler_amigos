from django.urls import path
from . import views

urlpatterns = [
    path('', views.editar_datos_cliente, name='editarPerfilCliente'),
    path('actualizar_datos/', views.actualizar_datos, name='actualizar_datos'),
]