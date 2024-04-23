from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes

urlpatterns = [
    path('programar/<amigo_id>/', views.programarSalida, name="ProgramarSalida"), 
    path('escogerHora/<categoria>/<fecha>/<descripcion>/<amigo_id>/<cliente_id>/', views.escogerHora, name="EscogerHora"),
    path('cancelar_programar_cita/', views.cancelar_programar_cita, name='cancelar_programar_cita'),
    path('cancelar_programar_cita2/', views.cancelar_programar_cita2, name='cancelar_programar_cita2'),
    path('confirmar_programar_cita/', views.confirmar_programar_cita, name='confirmar_programar_cita'),
    path('confirmar_programar_cita/<str:datos>/', views.confirmar_programar_cita, name='confirmar_programar_cita'),
]