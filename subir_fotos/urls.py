from django.urls import path
from . import views


urlpatterns = [
        path('subir_foto', views.cargar_fotos_perfil, name='subir_foto'),
        
        path('cancelar_subir_fotos/', views.cancelar_subir_fotos, name='cancelar_subir_fotos'),
]