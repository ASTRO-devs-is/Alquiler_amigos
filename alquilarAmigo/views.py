from django.shortcuts import render
from .forms import formularioCategoria
# Create your views here.

def programarSalida(request):
    formulario_categoria = formularioCategoria()
    return render(request, 'programarSalida/programarSalida.html', {'formCateg': formulario_categoria})