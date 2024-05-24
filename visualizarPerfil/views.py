from django.shortcuts import render
from alquilarAmigo.models import Amigo, Direccion, Tarifa, Cliente
from subir_fotos.models import FotoPerfil
from datetime import date

# Create your views here.
def visualizarPerfilAmigo(request, amigo_id=None):
    userEmail = request.user
    amigo = Amigo.objects.get(id=amigo_id)
    edad = date.today().year - amigo.fecha_nacimiento.year
    foto_perfil = FotoPerfil.objects.filter(fotos=amigo).first()
    amigo.foto = foto_perfil.image.url
    amigo.edad = edad
    amigo.pais = Direccion.objects.get(id=amigo.ubicacion_id).pais
    amigo.tarifa = Tarifa.objects.get(id=amigo.id_tarifa_id).tarifa
    amigo.genero = mostrarGenero(amigo.genero)
    return render(request, 'visualizarPerfil/visualizarPerfil.html', {'amigo': amigo, 'userEmail': str(userEmail)})

def mostrarGenero(genero):
    if genero == 2:
        return 'Masculino'
    elif genero == 1:
        return 'Femenino'
    else:
        return 'Otro'
    
def visualizarPerfilCliente(request, cliente_id=None):
    cliente = Cliente.objects.get(id=cliente_id)
    edad = date.today().year - cliente.fecha_nacimiento.year
    foto_perfil = FotoPerfil.objects.filter(fotosCliente=cliente).first()
    cliente.foto = foto_perfil.image.url
    cliente.edad = edad
    cliente.pais = Direccion.objects.get(id=cliente.ubicacion_id).pais
    cliente.genero = mostrarGenero(cliente.genero)
    return render(request, 'visualizarPerfil/perfilCliente.html', {'amigo': cliente})