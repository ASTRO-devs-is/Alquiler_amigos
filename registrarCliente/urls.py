from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('fotoCliente/<idCliente>', views.cargar_fotos_perfil, name='fotoCliente'),
]