from django.shortcuts import render, redirect
from .forms import formularioRegistrarAmigo
from urllib.parse import quote, unquote

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
            genero = request.POST['genero']  #agregar campo genero y obtenerlo del formulario pero en tipo numerico
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            descripcion_codificada = quote(descripcion)

            

            return redirect('subir_foto', nombre=nombre, apellido=apellido, ciudad=ciudad,
                                        pais=pais, telefono=telefono, email=email, localidad=localidad,
                                        descripcion=descripcion_codificada, fecha=fecha,tarifa=tarifa, genero = genero)
        return render(request, "registrarAmigo/registrarAmigo.html", {'form': form, 'errores': form.errors})
    return render(request, "registrarAmigo/registrarAmigo.html", {'form': formulario})

def aniadirHoras(request):
    return render(request, "aniadirHoras/aniadirHoras.html")

def cancelar_aniadir_horas(request):
    return render(request, 'aniadirHoras/cancelar.html')