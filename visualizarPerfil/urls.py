from django.urls import path
from . import views

urlpatterns = [
    path('amigo/<amigo_id>', views.visualizarPerfilAmigo, name="Visualizar_amigo"), 
]