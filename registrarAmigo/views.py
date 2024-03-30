from django.shortcuts import render
from .forms import formularioRegistrarAmigo

# Create your views here.
def registrarAmigo(request):
    formulario = formularioRegistrarAmigo()
    return render(request, "registrarAmigo/registrarAmigo.html", {'form': formulario})