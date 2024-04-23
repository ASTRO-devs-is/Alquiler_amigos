from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes

urlpatterns = [
    path('', views.inicio_login, name='inicio_login'),
    path('E_l/', views.login_view, name='login'),  # Para procesar los datos del formulario de login
]