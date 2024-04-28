from django.shortcuts import render
from alquilarAmigo.models import Amigo,Tarifa
from subir_fotos.models import FotoPerfil
from django.db.models import Q
from django.http import JsonResponse
import datetime

from django.core.paginator import Paginator

def inicio(request):
    respuestajson = buscarAmigos(request)

    return render(request, 'inicio/inicio.html', {'respuestajson': respuestajson})

from django.core import serializers

def buscarAmigos(request):
    nombre = request.GET.get('nombre')
    amigos = Amigo.objects.all().order_by('id')

    if nombre:
        lista = nombre.split(' ', 1)
        if len(lista) == 2:
            nombre = lista[0]
            apellido = lista[1]
            amigos = amigos.filter(Q(nombre__icontains=nombre) & Q(apellido__icontains=apellido))
        else:
            amigos = amigos.filter(nombre__icontains=nombre)
    amigos = amigos.order_by('nombre')
    paginator = Paginator(amigos, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    #print(page_number)

    amigos_serialized = []
    for amigo in page:
        amigo_data = {
            'nombre': amigo.nombre,
            'apellido': amigo.apellido,
            'correo': amigo.correo,
            'id': amigo.id,
            'edad':  datetime.datetime.now().year - amigo.fecha_nacimiento.year,
            'disponibilidad': amigo.disponibilidad,
        }

        amigo.tarifa = Tarifa.objects.get(id=amigo.id_tarifa_id).tarifa
        if amigo.tarifa:
            amigo_data['tarifa'] = amigo.tarifa
        else:
            amigo_data['tarifa'] = None

        foto_perfil = amigo.fotoperfil_set.first()
        if foto_perfil:
            amigo_data['foto'] = foto_perfil.image.url
        else:
            amigo_data['foto'] = None
        amigos_serialized.append(amigo_data)
        #print(amigo_data)

    data = {
        'amigos': amigos_serialized,
        'num_pages': paginator.num_pages,
        'has_previous': page.has_previous(),
        'has_next': page.has_next(),
        'page_number': page.number,
        'page_range': list(paginator.page_range)
    }
    return JsonResponse(data)


