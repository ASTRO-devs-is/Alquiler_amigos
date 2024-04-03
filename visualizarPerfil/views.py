from django.shortcuts import render
from alquilarAmigo.models import Amigo
from subir_fotos.models import FotoPerfil
from datetime import date

# Create your views here.
def visualizarPerfilAmigo(request, amigo_id=None, cliente_id=1):
    amigo = Amigo.objects.get(id=amigo_id)
    edad = date.today().year - amigo.fecha.year
    foto_perfil = FotoPerfil.objects.filter(fotos=amigo).first()
    amigo.foto = foto_perfil.image.url
    amigo.edad = edad
    return render(request, 'visualizarPerfil/visualizarPerfil.html', {'amigo': amigo})