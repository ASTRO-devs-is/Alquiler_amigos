from django.shortcuts import render
from .forms import formularioProgramarCita
import datetime
from .models import DisponibilidadHoras, Salida
# Create your views here.

def programarSalida(request):
    
    horas = calcularHorario()   
    formulario_programarSalida = formularioProgramarCita()
    if request.method == 'POST':
        formulario_datos = formularioProgramarCita(request.POST)
        if formulario_datos.is_valid():
            #formulario_datos.save()
            categorias = request.POST.get('categorias')
            fecha = request.POST.get('fecha')
            cajaTexto = request.POST.get('cajaTexto')
            horaInicio = request.POST.get('horaInicio')
            horaFin = request.POST.get('horaFin')
            datos = {'categorias': categorias, 'fecha': fecha, 'cajaTexto': cajaTexto, 'horaInicio': horaInicio, 'horaFin': horaFin}
            return render(request, "programarSalida/respuesta.html", {'datos': datos})
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
            if salida.horaInicio >= hora.horaInicio and salida.horaFin <= hora.horaFin:
                horas = horas.exclude(id=hora.id)
                

    return horas