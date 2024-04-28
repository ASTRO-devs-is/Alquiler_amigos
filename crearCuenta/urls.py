from django.urls import path
from . import views

urlpatterns = [
    path('cuenta/', views.crearCuenta, name="crearCuenta"), 
]