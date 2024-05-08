from django.shortcuts import render, redirect
from .forms import formularioProgramarCita
from datetime import datetime
from .models import DisponibilidadHoras, Salida, Categoria,Amigo, Cliente
import json
# Create your views here.

def programarSalida(request, amigo_id=None ):
    usuario=request.user
    try:
        usuarioAmigo = Amigo.objects.get(correo=usuario.email)
    except:
        usuarioAmigo = None
    if(usuarioAmigo == None):
        usuarioAmigo = Cliente.objects.get(correo=usuario.email)
    cliente_id = usuarioAmigo.id
    formulario_programarSalida = formularioProgramarCita()
    if request.method == 'POST':
        formulario_datos = formularioProgramarCita(request.POST)
        if formulario_datos.is_valid():
            
            categoria = request.POST.get('categorias')
            fecha = request.POST.get('fecha')
            descripcion = request.POST.get('descripcion')

            return redirect('EscogerHora', categoria=categoria, fecha=fecha, descripcion=descripcion, amigo_id=amigo_id, cliente_id=cliente_id)
        else:
            return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_datos, 'errores': formulario_datos.errors})
            
                
    return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_programarSalida})

def escogerHora(request, categoria, fecha, descripcion, amigo_id, cliente_id):
    salidas = Salida.objects.filter(amigo_id=amigo_id, cliente_id=cliente_id, fecha_salida=fecha)
    horas = calcularHorario(fecha = fecha, amigo_id = amigo_id, cliente_id = cliente_id)
    
    datos = []
    
    horarios_seleccionados = request.POST.getlist('horario_seleccionado')
    if len(horarios_seleccionados) != 0:
        if request.method == 'POST':
            for horario_id in horarios_seleccionados:
                horario = DisponibilidadHoras.objects.get(id=horario_id)
                datos.append({'categoria': categoria, 'fecha': fecha, 'descripcion': descripcion, 'amigo_id': amigo_id, 'cliente_id': cliente_id,
                        'hora_inicio': str(horario.horaInicio), 'hora_fin': str(horario.horaFin)})
            datos_json = json.dumps(datos)
            return redirect('confirmar_programar_cita', datos=datos_json)
            
    return render(request, 'programarSalida/escogerHora.html', {'horas': horas, 'salidas': salidas})

def calcularHorario(fecha, amigo_id, cliente_id):
    ahora = datetime.now()
    # Comprueba si la fecha es hoy
    if fecha == str(ahora.date()):
        # Si la fecha es hoy, solo retorna los horarios a partir de la hora actual
        horas = DisponibilidadHoras.objects.filter(amigo_id=amigo_id, horaInicio__gte=ahora.time())
    else:
        # Si la fecha no es hoy, retorna todos los horarios
        horas = DisponibilidadHoras.objects.filter(amigo_id=amigo_id)

    #horas = DisponibilidadHoras.objects.filter(amigo_id=amigo_id)  
    salidas = Salida.objects.filter(amigo_id=amigo_id, cliente_id=cliente_id, fecha_salida=fecha)
    horas_disponibles = []
    for hora in horas:
        conflicto = False
        for salida in salidas:
            if (salida.hora_inicio_salida < hora.horaFin) and (salida.hora_fin_salida > hora.horaInicio):
                conflicto = True
                break
        if not conflicto:
            horas_disponibles.append(hora)

    return horas_disponibles


def cancelar_programar_cita(request):
    return render(request, 'programarSalida/cancelar.html')

def cancelar_programar_cita2(request):
    return render(request, 'programarSalida/cancelar2.html')

def confirmar_programar_cita(request, datos=None):
    datos_nuevos = json.loads(datos)
    if request.method == 'POST':
        for dato in datos_nuevos:
            nueva_salida = Salida()
            nueva_salida.cliente_id = dato['cliente_id']
            nueva_salida.amigo_id = dato['amigo_id']
            nueva_salida.descripcion_salida = dato['descripcion']
            nueva_salida.categoria_salida_id = Categoria.objects.get(nombre=dato['categoria']).id
            nueva_salida.fecha_salida = datetime.strptime(dato['fecha'], '%Y-%m-%d')
            nueva_salida.hora_inicio_salida = datetime.strptime(dato['hora_inicio'], '%H:%M:%S')
            nueva_salida.hora_fin_salida = datetime.strptime(dato['hora_fin'], '%H:%M:%S')
            nueva_salida.save()
        return redirect('Inicio')
    return render(request, 'programarSalida/confirmar.html', {'salidas': datos_nuevos})