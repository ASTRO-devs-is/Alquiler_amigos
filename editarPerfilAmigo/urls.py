from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes

urlpatterns = [
    path('', views.registrarAmigo, name="RegistrarAmigo"),  
    path('aniadirHoras', views.aniadirHoras, name="AniadirHoras"),
    path('cancelHoras', views.cancelar_aniadir_horas, name="cancelar_aniadir_horas"),  
    path('politicas', views.politicadeprivacidad, name="politicas"),
    path('terminos', views.terminosycondiciones, name="terminos"),
]