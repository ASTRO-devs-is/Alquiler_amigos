from django.shortcuts import render
from alquilarAmigo.models import Amigo
from subir_fotos.models import FotoPerfil

# Create your views here.
def inicio(request):
    amigos = Amigo.objects.all()

    for amigo in amigos:
        foto_perfil = FotoPerfil.objects.filter(fotos=amigo).first()
        if foto_perfil:
            amigo.foto = foto_perfil.image.url
        else:
            amigo.foto = None
    
    return render(request, 'inicio/inicio.html', {'amigos': amigos})