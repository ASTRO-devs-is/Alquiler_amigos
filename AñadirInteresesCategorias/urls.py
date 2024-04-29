from django.urls import path
from . import views

urlpatterns = [
    path('guardar-intereses-categorias/', views.guardar_intereses_categorias, name='guardar_intereses_categorias'),
    # Otras URLs de tu aplicación
]
