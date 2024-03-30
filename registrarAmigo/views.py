from django.shortcuts import render
from .forms import formularioRegistrarAmigo

# Create your views here.
def registrarAmigo(request):
    formulario = formularioRegistrarAmigo()
    if request.method == 'POST':
        form = formularioRegistrarAmigo(request.POST)
        if form.is_valid():
            nombre =request.POST['nombre']
            apellido = request.POST['apellido']
            ciudad = request.POST['ciudad']
            pais = request.POST['pais']
            telefono = request.POST['telefono']
            email = request.POST['email']
            localidad = request.POST['localidad']
            tarifa = request.POST['tarifa']
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            datos = {'nombre': nombre, 'apellido': apellido, 'ciudad': ciudad, 'pais': pais, 
                    'telefono': telefono, 'email': email, 'localidad': localidad, 'tarifa': tarifa,
                    'descripcion': descripcion, 'fecha': fecha}
            return render(request, "registrarAmigo/respuesta.html", {'datos': datos})
        return render(request, "registrarAmigo/registrarAmigo.html", {'form': form, 'errores': form.errors})
    return render(request, "registrarAmigo/registrarAmigo.html", {'form': formulario})