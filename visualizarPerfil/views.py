from django.shortcuts import render
from alquilarAmigo.models import Amigo, Direccion, Tarifa
from subir_fotos.models import FotoPerfil
from datetime import date

# Create your views here.
def visualizarPerfilAmigo(request, amigo_id=None, cliente_id=1):
    amigo = Amigo.objects.get(id=amigo_id)
    edad = date.today().year - amigo.fecha_nacimiento.year
    foto_perfil = FotoPerfil.objects.filter(fotos=amigo).first()
    amigo.foto = foto_perfil.image.url
    amigo.edad = edad
    amigo.pais = Direccion.objects.get(id=amigo.ubicacion_id).pais
    amigo.tarifa = Tarifa.objects.get(id=amigo.id_tarifa_id).tarifa
    amigo.genero = mostrarGenero(amigo.genero)
    return render(request, 'visualizarPerfil/visualizarPerfil.html', {'amigo': amigo})

def mostrarGenero(genero):
    if genero == 1:
        return 'Masculino'
    elif genero == 2:
        return 'Femenino'
    else:
        return 'Otro'