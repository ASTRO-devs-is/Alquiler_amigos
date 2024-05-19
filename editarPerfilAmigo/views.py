from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo
from django.contrib import messages
from alquilarAmigo.models import  Amigo,User
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm

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
'''
def editar (request, id_amigo):
   amigo = get_object_or_404(Amigo, id=id_amigo)
   #amigo = Amigo.objects.get(id=id_amigo)
   #data = {
     # 'form':formularioAmigo(instance=amigo),
   #   'fecha_nacimiento': amigo.fecha_nacimiento
  # }
   form = formularioAmigo(instance=amigo)
   print("Fecha Nacimiento")
   print(amigo.fecha_nacimiento)
   return render(request, "editarPerfilAmigo/editarPerfilAmigo.html", {'form': form, 'amigo': amigo,'id_amigo': id_amigo})
   #return render(request, "editarPerfilAmigo/editarPerfilAmigo.html",data)
'''
def editar(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)

    # Verificar si el amigo ya tiene una foto de perfil o crear una nueva instancia
    if hasattr(amigo, 'fotoperfil'):
        foto_form = FotoPerfilForm(instance=amigo.fotoperfil)
    else:
        foto_form = FotoPerfilForm()

    if request.method == 'POST':
        form = formularioAmigo(request.POST, instance=amigo)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=amigo.fotoperfil if hasattr(amigo, 'fotoperfil') else None)

        if form.is_valid() and foto_form.is_valid():
            form.save()
            foto_perfil = foto_form.save(commit=False)
            foto_perfil.fotos = amigo
            foto_perfil.save()
            messages.success(request, 'Perfil actualizado con éxito')
            return redirect('perfil', id_amigo=amigo.id)
    else:
        form = formularioAmigo(instance=amigo)

    return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
        'form': form,
        'foto_form': foto_form,
        'amigo': amigo,
        'id_amigo': id_amigo,
    })