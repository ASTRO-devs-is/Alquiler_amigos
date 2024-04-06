from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
        path('subir_foto/<nombre>/<apellido>/<ciudad>/<pais>/<telefono>/<email>/<localidad>/<descripcion>/<fecha>/<tarifa>/<genero>',
            views.cargar_fotos_perfil, name='subir_foto'),
]