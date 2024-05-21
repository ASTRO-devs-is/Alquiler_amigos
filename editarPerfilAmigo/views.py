from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo
from django.contrib import messages
from alquilarAmigo.models import  Amigo,User,Direccion
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm
from django.core.exceptions import ValidationError

# Create your views here.

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
