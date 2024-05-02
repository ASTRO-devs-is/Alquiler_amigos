from django.urls import path
from . import views


urlpatterns = [
      path('<nombre>/<apellido>/<ciudad>/<pais>/<telefono>/<email>/<localidad>/<descripcion>/<fecha>/<tarifa>/<genero>/<contraseña>/',
            views.cargar_fotos_perfil, name='subir_foto'),
     #path('subir_fotos/', views.cargar_fotos_perfil, name='subir_foto'),
        
      path('cancelar_subir_fotos/', views.cancelar_subir_fotos, name='cancelar_subir_fotos'),
]