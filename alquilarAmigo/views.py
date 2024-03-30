from django.shortcuts import render
from .forms import formularioProgramarCita
import datetime
from .models import DisponibilidadHoras, Salida, Categoria
# Create your views here.

def programarSalida(request):
    
    horas = calcularHorario()   
    formulario_programarSalida = formularioProgramarCita()
    if request.method == 'POST':
        formulario_datos = formularioProgramarCita(request.POST)
        if formulario_datos.is_valid():
            nueva_salida = Salida()
            nombre_categoria = request.POST.get('categorias')
            categoria = Categoria.objects.get(nombre=nombre_categoria)
            nueva_salida.categoria = categoria
            nueva_salida.fecha = request.POST.get('fecha')
            nueva_salida.cajaTexto = request.POST.get('cajaTexto')
            nueva_salida.horaInicio = request.POST.get('horaInicio')
            nueva_salida.horaFin = request.POST.get('horaFin')
            nueva_salida.amigo_id = obtenerAmigoId()
            nueva_salida.cliente_id = obtenerClienteId()
            nueva_salida.save()
        else:
            return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_datos, 
                                                                            'horas': horas, 'errores': formulario_datos.errors})
            
                
    return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_programarSalida, 
                                                                    'horas': horas})

def calcularHorario():
    amigo_id = 1  # Reemplaza esto con el id del amigo que quieres filtrar
    cliente_id = 1  # Reemplaza esto con el id del cliente que quieres filtrar
    horas = DisponibilidadHoras.objects.filter(amigo_id=amigo_id)  
    salidas = Salida.objects.filter(amigo_id=amigo_id, cliente_id=cliente_id)

    for salida in salidas:
        for hora in horas:
            if (salida.horaInicio >= hora.horaInicio and salida.horaFin <= hora.horaFin) :
                horas = horas.exclude(id=hora.id)
                

    return horas

def obtenerAmigoId():
    return 1  # Reemplaza esto con el id del amigo que quieres asignar
def obtenerClienteId():
    return 1  # Reemplaza esto con el id del cliente que quieres asignar
