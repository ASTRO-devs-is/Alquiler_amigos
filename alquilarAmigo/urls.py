from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes

urlpatterns = [
    path('programar', views.programarSalida, name="ProgramarSalida"), 
    path('escogerHora/<categoria>/<fecha>/<cajaTexto>/<amigo_id>/<cliente_id>/', views.escogerHora, name="EscogerHora"),
]