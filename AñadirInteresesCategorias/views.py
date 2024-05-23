from django.http import JsonResponse
from alquilarAmigo.models import Interes, Categoria
from django.shortcuts import render, redirect
import json

def saveDates(request):
    if request.method == 'POST':
        # Obtener los datos enviados desde el frontend
        intereses = request.POST.getlist('intereses[]')
        categorias = request.POST.getlist('categorias[]')

        # Guardar los intereses y categorías en la base de datos
        for interes in intereses:
            # Verificar si el interés ya existe antes de crearlo nuevamente
            if not Interes.objects.filter(nombre=interes).exists():
                Interes.objects.create(nombre=interes)
        
        for categoria in categorias:
            # Verificar si la categoría ya existe antes de crearla nuevamente
            if not Categoria.objects.filter(nombre=categoria).exists():
                Categoria.objects.create(nombre=categoria)

        # Enviar una respuesta JSON al frontend
        response_data = {'message': 'Datos guardados correctamente'}
        #return JsonResponse(response_data)
    return render(request, 'intereses_categorias.html')
    #else:
    #    # La solicitud no es POST, devolver un error
    #    response_data = {'error': 'Solicitud no válida'}
    #    return JsonResponse(response_data, status=400)

def categoria_Intereses(request, id_amigo):
    categorias = list(Categoria.objects.all().values_list('nombre', flat=True))
    intereses = list(Interes.objects.all().values_list('interes', flat=True))
    print("hola")

    context = {
        'categorias': json.dumps(categorias),
        'intereses': json.dumps(intereses)
    }

    return render(request, 'intereses_categorias.html', context)
