from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes

urlpatterns = [
   path('editar/<int:id_amigo>/', views.editar, name="editarAmigo"), 
   path('editar_horas/<int:id_amigo>/', views.editar_anadir_horas, name="editarHorasAmigo"),   
]