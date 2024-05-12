from django.shortcuts import render
from alquilarAmigo.models import Amigo,Tarifa, User, Categoria, User_Categoria, Interes, Categoria_Interes
from subir_fotos.models import FotoPerfil
from django.db.models import Q
from django.http import JsonResponse
import datetime
from django.core import serializers

from django.core.paginator import Paginator

def inicio(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    intereses = Interes.objects.all()
    respuestajson = buscarAmigos(request)
    
    return render(request, 'inicio/inicio.html', {'categorias': categorias, 'intereses': intereses, 'respuestajson': respuestajson})

def buscarAmigos(request):
    nombre = request.GET.get('nombre')
    categorias_raw = request.GET.get('categorias', '')
    intereses_raw = request.GET.get('intereses', '')
    
    # Dividir las cadenas de categorías e intereses en listas
    categorias = categorias_raw.split(',')
    intereses = intereses_raw.split(',')
    
    # Intentar convertir cada valor a entero, ignorando los valores no válidos
    categorias = [int(c) for c in categorias if c.strip() and c.strip().isdigit()]
    intereses = [int(i) for i in intereses if i.strip() and i.strip().isdigit()]

    amigos = Amigo.objects.all().order_by('id')
    if nombre:
        lista = nombre.split(' ', 1)
        if len(lista) == 2:
            nombre = lista[0]
            apellido = lista[1]
            amigos = amigos.filter(Q(nombre__icontains=nombre) & Q(apellido__icontains=apellido))
        else:
            amigos = amigos.filter(nombre__icontains=nombre)

    # Verificar si la lista de categorías no está vacía
    if categorias:
        usuarios_con_categorias = User_Categoria.objects.filter(categoria__in=categorias).values_list('user', flat=True)
        correos = User.objects.filter(id__in=usuarios_con_categorias).values_list('email', flat=True)
        amigos = amigos.filter(correo__in=correos)
    else:
        # Si la lista de categorías está vacía, no aplicar ningún filtro
        pass

    # Verificar si la lista de intereses no está vacía
    if intereses:
        categorias_con_intereses= Categoria_Interes.objects.filter(interes__in=intereses).values_list('categoria', flat=True)
        usuarios_con_intereses = User_Categoria.objects.filter(categoria__in=categorias_con_intereses).values_list('user', flat=True)
        correos = User.objects.filter(id__in=usuarios_con_intereses).values_list('email', flat=True)
        amigos = amigos.filter(correo__in=correos)
    else:
        # Si la lista de intereses está vacía, no aplicar ningún filtro
        pass

    amigos = amigos.order_by('nombre')
    paginator = Paginator(amigos, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

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

    data = {
        'amigos': amigos_serialized,
        'num_pages': paginator.num_pages,
        'has_previous': page.has_previous(),
        'has_next': page.has_next(),
        'page_number': page.number,
        'page_range': list(paginator.page_range),
    }
    return JsonResponse(data)





