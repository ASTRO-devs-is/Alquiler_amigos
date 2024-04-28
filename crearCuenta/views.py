from django.shortcuts import render
from alquilarAmigo.models import Amigo, Direccion, Tarifa
from subir_fotos.models import FotoPerfil
from datetime import date

# Create your views here.
def crearCuenta(request):
    return render(request, 'crearCuenta/crearCuenta.html')