from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizarAlquiler, name='visualizarAlquiler'),
    path('cambiar_estado_salida/', views.cambiar_estado_salida, name='cambiar_estado_salida'),
]