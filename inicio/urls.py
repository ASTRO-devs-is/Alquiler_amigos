from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('buscar/', views.buscarAmigos, name="Buscar"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]