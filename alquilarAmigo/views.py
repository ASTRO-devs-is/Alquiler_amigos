from django.shortcuts import render
from .forms import formularioProgramarCita
# Create your views here.

def programarSalida(request):
    formulario_categoria = formularioProgramarCita()
    return render(request, 'programarSalida/programarSalida.html', {'formCateg': formulario_categoria})