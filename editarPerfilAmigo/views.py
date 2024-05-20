from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo
from django.contrib import messages
from alquilarAmigo.models import  Amigo,User,Direccion
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm
from django.core.exceptions import ValidationError

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
def editar123(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
   
    # Verificar si el amigo ya tiene una foto de perfil o crear una nueva instancia
   # if hasattr(amigo, 'fotoperfil'):
    #    foto_form = FotoPerfilForm(instance=amigo.fotoperfil)
    #else:
     #   foto_form = FotoPerfilForm()
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=amigo)
    foto_form = FotoPerfilForm(instance=foto_perfil)


    if request.method == 'POST':
        form = formularioAmigo(request.POST, instance=amigo)
        #foto_form = FotoPerfilForm(request.POST, request.FILES, instance=amigo.fotoperfil if hasattr(amigo, 'fotoperfil') else None)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=foto_perfil)

        if form.is_valid() and foto_form.is_valid():

            telefono = form.cleaned_data['telefono']
            amigo = form.save(commit=False)
            direccion = Direccion.objects.create(
                pais=form.cleaned_data['pais'],
                ciudad=form.cleaned_data['ciudad'],
                localidad=form.cleaned_data['localidad'],
                
            )
            amigo.ubicacion = direccion
            if Amigo.objects.exclude(id=id_amigo).filter(telefono=telefono).exists():
                return render(request, 'editarPerfilAmigo.html', {'form': form, 'telefonoRepetido': 'Este telefono ya esta registrado'})
            else:
                amigo.save()
                #return redirect('Inicio')
                form.save()
                foto_perfil = foto_form.save(commit=False)
                foto_perfil.image = amigo
                foto_perfil.save()
                messages.success(request, 'Perfil actualizado con éxito')
                return redirect('Inicio', id_amigo=amigo.id)
    else:
        form = formularioAmigo(instance=amigo)

    return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
        'form': form,
        'foto_form': foto_form,
        'amigo': amigo,
        'foto_perfil': foto_perfil,
        'id_amigo': id_amigo,
    })

def editarPrueba(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=amigo)
    foto_form = FotoPerfilForm(instance=foto_perfil)

    if request.method == 'POST':
        form = formularioAmigo(request.POST, instance=amigo)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=foto_perfil)

        if form.is_valid() and foto_form.is_valid():
            # Validar teléfono duplicado
            telefono = form.cleaned_data['telefono']
            if Amigo.objects.exclude(id=id_amigo).filter(telefono=telefono).exists():
                return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
                    'form': form,
                    'foto_form': foto_form,
                    'amigo': amigo,
                    'foto_perfil': foto_perfil,
                    'id_amigo': id_amigo,
                    'telefonoRepetido': 'Este teléfono ya está registrado'
                })

            # Guardar amigo y dirección
            amigo = form.save(commit=False)
            direccion = Direccion.objects.create(
                pais=form.cleaned_data['pais'],
                ciudad=form.cleaned_data['ciudad'],
                localidad=form.cleaned_data['localidad'],
            )
            amigo.ubicacion = direccion
            amigo.save()

            # Guardar foto de perfil
            foto_perfil = foto_form.save(commit=False)
            foto_perfil.fotos = amigo
            foto_perfil.save()

            messages.success(request, 'Perfil actualizado con éxito')
            return redirect('Inicio')  # Asegúrate de que 'Inicio' sea la URL correcta

    else:
        form = formularioAmigo(instance=amigo)

    return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
        'form': form,
        'foto_form': foto_form,
        'amigo': amigo,
        'foto_perfil': foto_perfil,
        'id_amigo': id_amigo,
    })

def editarPruebaNuevamente(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=amigo)
    foto_form = FotoPerfilForm(instance=foto_perfil)

    if request.method == 'POST':
        form = formularioAmigo(request.POST, instance=amigo)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=foto_perfil)
        print("Estamos en POST")
        print(form.is_valid())
        print(foto_form.is_valid())
        print(form.errors)
        if form.is_valid() and foto_form.is_valid():
            form.save()
            print("ESTAMOS AQUI")
            foto_perfil = foto_form.save(commit=False)
            foto_perfil.fotos = amigo
            foto_perfil.save()
            messages.success(request, 'Perfil actualizado con éxito')
           # return redirect('Inicio', id_amigo=amigo.id)
            return redirect(to='Inicio')
    else:
        form = formularioAmigo(instance=amigo)

    return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
        'form': form,
        'foto_form': foto_form,
        'amigo': amigo,
        'foto_perfil': foto_perfil,
        'id_amigo': id_amigo,
    })
def editar(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=amigo)
    foto_form = FotoPerfilForm(instance=foto_perfil)

    if request.method == 'POST':
        form = formularioAmigo(request.POST, instance=amigo)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=foto_perfil)

        # Validar el formulario amigo manualmente para el campo telefono
        telefono_cambiado = False
        if 'telefono' in form.changed_data:
            telefono_cambiado = True
        print("Estamos en POST")
        print(form.is_valid())
        print(foto_form.is_valid())
        print(form.errors)
        if form.is_valid():
            if telefono_cambiado:
                # Validar teléfono manualmente si ha cambiado
                telefono = form.cleaned_data['telefono']
                if Amigo.objects.filter(telefono=telefono).exclude(id=amigo.id).exists():
                    form.add_error('telefono', 'Este número de teléfono ya está registrado')
            # Si no hay errores, considerar el formulario válido
            if not form.errors and foto_form.is_valid():
                form.save()
                foto_perfil = foto_form.save(commit=False)
                foto_perfil.fotos = amigo
                foto_perfil.save()
                messages.success(request, 'Perfil actualizado con éxito')
                return redirect('Inicio')
        else:
            print("Errores en el formulario:", form.errors)

    else:
        form = formularioAmigo(instance=amigo)

    return render(request, 'editarPerfilAmigo/editarPerfilAmigo.html', {
        'form': form,
        'foto_form': foto_form,
        'amigo': amigo,
        'foto_perfil': foto_perfil,
        'id_amigo': id_amigo,
    })
