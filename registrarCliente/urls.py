from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('exito/', views.exito_registro, name='exito_registro'),
]