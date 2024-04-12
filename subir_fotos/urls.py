from django.urls import path
from . import views


urlpatterns = [
        path('<nombre>/<apellido>/<ciudad>/<pais>/<telefono>/<email>/<localidad>/<path:descripcion>/<fecha>/<tarifa>/<genero>',
            views.cargar_fotos_perfil, name='subir_foto'),
        
        path('cancelar_subir_fotos/', views.cancelar_subir_fotos, name='cancelar_subir_fotos'),
        path('exito/', views.exito, name='exito'),
        path('exito/<str:datos>', views.exito, name='exito'),
]