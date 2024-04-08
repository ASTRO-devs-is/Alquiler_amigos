from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cargar_fotos_perfil, exito

urlpatterns = [
    path('cargar_fotos_perfil/', cargar_fotos_perfil, name='cargar_fotos_perfil'),
    path('exito/', exito, name='exito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
