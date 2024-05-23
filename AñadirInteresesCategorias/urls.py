from django.urls import path
from . import views

urlpatterns = [
    path('guardar-intereses-categorias/', views.categoria_Intereses, name='guardar_intereses_categorias'),
]