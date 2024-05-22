from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_usuario>/', views.editarCliente, name='editarCliente'),
    #path('actualizar_datos/<int:id_usuario>/', views.actualizar_datos, name='actualizar_datos'),
    #path('<int:id_usuario>/', views.actualizar_datos, name='actualizar_datos'),
]