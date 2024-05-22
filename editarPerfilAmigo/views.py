from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo
from django.contrib import messages
from alquilarAmigo.models import  Amigo,User,Direccion,DisponibilidadHoras
from django.forms import modelformset_factory
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

def editar_anadir_horas123(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
    DisponibilidadHorasFormSet = modelformset_factory(DisponibilidadHoras, fields=('horaInicio', 'horaFin'), extra=1, can_delete=True)
    
    if request.method == 'POST':
        formset = DisponibilidadHorasFormSet(request.POST, queryset=DisponibilidadHoras.objects.filter(amigo=amigo))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.amigo = amigo
                instance.save()
            for instance in formset.deleted_objects:
                instance.delete()
            messages.success(request, 'Disponibilidad de horas actualizada con éxito')
            return redirect('editarAmigo', id_amigo=amigo.id)
    else:
        formset = DisponibilidadHorasFormSet(queryset=DisponibilidadHoras.objects.filter(amigo=amigo))
    
    return render(request, 'aniadirHoras/editarDisponibilidadHoras.html', {
        'formset': formset,
        'amigo': amigo
    })

def editar_anadir_horas(request, id_amigo):
    amigo = get_object_or_404(Amigo, id=id_amigo)
    
    # Generar opciones de horas en el formato 'Desde 08:00 Hasta 09:00'
    horas_disponibles = ["Desde {:02d}:00 Hasta {:02d}:00".format(h, h + 1) for h in range(8, 22)]
    
    # Obtener las horas seleccionadas previamente por el amigo
    horas_seleccionadas = DisponibilidadHoras.objects.filter(amigo=amigo)
    horas_seleccionadas_dict = {
        "Desde {} Hasta {}".format(hora.horaInicio.strftime('%H:%M'), hora.horaFin.strftime('%H:%M')): True 
        for hora in horas_seleccionadas
    }
    
    if request.method == 'POST':
        # Eliminar horas previas
        DisponibilidadHoras.objects.filter(amigo=amigo).delete()
        
        # Guardar nuevas horas seleccionadas
        horarios_seleccionados = []
        for i in range(1, len(horas_disponibles) + 1):
            horario = request.POST.get('horario_seleccionado_{}'.format(i))
            if horario:
                horarios_seleccionados.append(horario)
        
        for horario in horarios_seleccionados:
            horaInicio, horaFin = horario.split(" Hasta ")
            horaInicio = horaInicio.replace("Desde ", "")
            DisponibilidadHoras.objects.create(amigo=amigo, horaInicio=horaInicio, horaFin=horaFin)
        
        messages.success(request, 'Disponibilidad de horas actualizada con éxito')
        return redirect('editarAmigo', id_amigo=amigo.id)
    
    return render(request, 'aniadirHoras/editarDisponibilidadHoras.html', {
        'horas_disponibles': horas_disponibles,
        'horas_seleccionadas_dict': horas_seleccionadas_dict,
        'amigo': amigo
    })