from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioAmigo
from django.contrib import messages
from alquilarAmigo.models import  Amigo,User,Direccion,DisponibilidadHoras, Categoria, Interes, User_Categoria, User_Interes
from django.forms import modelformset_factory
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm
from django.core.exceptions import ValidationError
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.urls import reverse
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

def getCategInters(request, id_amigo):
    # Obtener el amigo
    amigo = get_object_or_404(User, pk=id_amigo)

    # Obtener los intereses del amigo
    intereses_amigo = User_Interes.objects.filter(user=amigo, activo_uc=True).values_list('interes__interes', flat=True)
    # Obtener las categorías del amigo
    categorias_amigo = User_Categoria.objects.filter(user=amigo, activo_uc=True).values_list('categoria__nombre', flat=True)

    # Obtener todos los intereses y categorías disponibles
    intereses_disponibles = list(Interes.objects.values_list('interes', flat=True))
    categorias_disponibles = list(Categoria.objects.values_list('nombre', flat=True))

    context = {
        'intereses_amigo': json.dumps(list(intereses_amigo)),
        'categorias_amigo': json.dumps(list(categorias_amigo)),
        'intereses_disponibles': json.dumps(intereses_disponibles),
        'categorias_disponibles': json.dumps(categorias_disponibles),
        'id_amigo': id_amigo
    }

    return render(request, 'aditarCategIntereses/editarCatInt.html', context)

def actualizar_categ_interes(request, id_amigo):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = get_object_or_404(User, pk=id_amigo)

            # Limpiar los intereses y categorías actuales del usuario
            User_Interes.objects.filter(user=user).delete()
            User_Categoria.objects.filter(user=user).delete()

            # Añadir los nuevos intereses
            for interes_name in data.get('interests', []):
                interes = get_object_or_404(Interes, interes=interes_name)
                User_Interes.objects.create(user=user, interes=interes)

            # Añadir las nuevas categorías
            for categoria_name in data.get('categories', []):
                categoria = get_object_or_404(Categoria, nombre=categoria_name)
                User_Categoria.objects.create(user=user, categoria=categoria)

            # Construir la URL de redirección
            redirect_url = reverse('editarAmigo', args=[id_amigo])
            response_data = {
                'status': 'success',
                'message': 'Datos actualizados correctamente',
                'redirect_url': redirect_url  # URL de redirección
            }
            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
