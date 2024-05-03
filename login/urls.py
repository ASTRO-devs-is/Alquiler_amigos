from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.inicio_login, name='inicio_login'),
    path('E_l/', views.login_view, name='login'),  # Para procesar los datos del formulario de login
]