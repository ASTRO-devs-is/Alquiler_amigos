from django.shortcuts import render, redirect
from .forms import ClienteForm
from alquilarAmigo.models import Cliente, Direccion, User
from django.shortcuts import get_object_or_404
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm
from django.contrib import messages


def editar_datos_cliente123(request, id_usuario):
    cliente = Cliente.objects.get(id=id_usuario)
    form = ClienteForm(instance=cliente)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=cliente)
    foto_form = FotoPerfilForm(instance=foto_perfil)
    if not cliente.id:
        return render(request, 'editarPerfilCliente.html', {'error': 'Cliente no encontrado'})
   
    return render(request, 'editarPerfilCliente.html', {'form': form, 'cliente': cliente, 'id_usuario': id_usuario,  'foto_form': foto_form,'foto_perfil': foto_perfil})


def actualizar_datos1234 (request,id_usuario):
        
    cliente = get_object_or_404(Cliente, id=id_usuario)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        #form = ClienteForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            cliente = form.save(commit=False)
            direccion = Direccion.objects.create(
                pais=form.cleaned_data['pais'],
                ciudad=form.cleaned_data['ciudad'],
                localidad=form.cleaned_data['localidad'],
                
            )
            cliente.ubicacion = direccion
            #Verificamos si el telefono existe en la base de datos
            #if Cliente.objects.filter(telefono=telefono).exists():
            if Cliente.objects.exclude(id=id_usuario).filter(telefono=telefono).exists():
                return render(request, 'editarPerfilCliente.html', {'form': form, 'telefonoRepetido': 'Este telefono ya esta registrado'})
            #elif Cliente.objects.filter(correo=direccion.correo).exists():
            #    return render(request, 'editarPerfilCliente.html', {'form': form, 'correoRepetido': 'Este correo ya esta registrado'})
            else:
                cliente.save()
                return redirect('Inicio')
    
    else:

        #form = ClienteForm()
        form = ClienteForm(instance=cliente)
    return render(request, 'editarPerfilCliente.html', {'form': form})
 
def editarCliente(request, id_usuario):
    cliente = get_object_or_404(Cliente, id=id_usuario)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotosCliente=cliente)
    foto_form = FotoPerfilForm(instance=foto_perfil)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
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
                if Cliente.objects.filter(telefono=telefono).exclude(id=cliente.id).exists():
                    form.add_error('telefono', 'Este número de teléfono ya está registrado')
            # Si no hay errores, considerar el formulario válido
            if not form.errors and foto_form.is_valid():
                form.save()
                foto_perfil = foto_form.save(commit=False)
                foto_perfil.fotosCliente = cliente
                foto_perfil.save()
                messages.success(request, 'Perfil actualizado con éxito')
                return redirect('Inicio')
        else:
            print("Errores en el formulario:", form.errors)

    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editarPerfilCliente.html', {
        'form': form,
        'foto_form': foto_form,
        'cliente': cliente,
        'foto_perfil': foto_perfil,
        'id_usuario': id_usuario,
    })

