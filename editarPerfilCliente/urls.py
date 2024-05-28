from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_usuario>/', views.editarCliente, name='editarCliente'),
    path('editar_CategInteresCli/<int:id_usuario>/', views.loadCategInters, name="Load"),  
    path('update/<int:id_usuario>/', views.update_categ_interes, name='Update'), 
    
]