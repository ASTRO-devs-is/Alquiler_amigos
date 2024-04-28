"""
URL configuration for alquilerAmigos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static#importamos estos dos para poder mostrar las imagenes
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),#incluye todas las urls de la app creada 
    path('alquilar/', include('alquilarAmigo.urls')),#incluye todas las urls de la app creada 
    path('registroAmigo/', include('registrarAmigo.urls')),#incluye todas las urls de la app creada
    path('subir_fotos/', include('subir_fotos.urls')),#incluye todas las urls de la app creada
    path('perfil/', include('visualizarPerfil.urls')),#incluye todas las urls de la app creada
    path('login/', include('login.urls')),
    path('cuenta/', include('crearCuenta.urls')),#incluye todas las urls de la app creada
    path('registroCliente/',include('registrarCliente.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#con esta linea de codigo le decimos a django que muestre las imagenes
