from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo

from alquilarAmigo.models import  Amigo,User

# Create your views here.
'''
def registrarAmigo(request):
    formulario = formularioAmigo()
    print('aquiesta')
    print(formulario['contrasena'])
    if request.method == 'POST':
        form = formularioAmigo(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
           # Convertir la fecha a un formato serializable
            fecha = form.cleaned_data['fecha'].isoformat()

            # Guardar los datos del formulario en la sesión
            request.session['datos_registro'] = {
                'nombre': form.cleaned_data['nombre'],
                'apellido': form.cleaned_data['apellido'],
                'ciudad': form.cleaned_data['ciudad'],
                'pais': form.cleaned_data['pais'],
                'telefono': form.cleaned_data['telefono'],
                'email': form.cleaned_data['email'],
                'localidad': form.cleaned_data['localidad'],
                'descripcion': quote(form.cleaned_data['descripcion']),
                'fecha': fecha,
                'tarifa': form.cleaned_data['tarifa'],
                'genero': form.cleaned_data['genero'],
                'contrasena': form.cleaned_data['contrasena']
            }

            #return redirect('subir_foto')
        return render(request, "editarPerfilAmigo/editarPerfilAmigo.html", {'form': form, 'errores': form.errors})
    return render(request, "editarPerfilAmigo/editarPerfilAmigo.html", {'form': formulario})
'''

def editar (request, id_amigo):
   amigo = get_object_or_404(Amigo, id=id_amigo)
   form = formularioAmigo(instance=amigo)
   return render(request, "editarPerfilAmigo/editarPerfilAmigo.html", {'form': form})