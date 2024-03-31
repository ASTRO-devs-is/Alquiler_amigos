from django.shortcuts import render, redirect
from .forms import formularioProgramarCita, FormularioHoras
import datetime
from .models import DisponibilidadHoras, Salida, Categoria
# Create your views here.

def programarSalida(request):
    
    formulario_programarSalida = formularioProgramarCita()
    if request.method == 'POST':
        formulario_datos = formularioProgramarCita(request.POST)
        if formulario_datos.is_valid():
            
            categoria = request.POST.get('categorias')
            fecha = request.POST.get('fecha')
            cajaTexto = request.POST.get('cajaTexto')
            amigo_id = obtenerAmigoId(request)
            cliente_id = obtenerClienteId()

            return redirect('EscogerHora', categoria=categoria, fecha=fecha, cajaTexto=cajaTexto, amigo_id=amigo_id, cliente_id=cliente_id)
        else:
            return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_datos, 'errores': formulario_datos.errors})
            
                
    return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_programarSalida})

def escogerHora(request, categoria, fecha, cajaTexto, amigo_id, cliente_id):
    #formulario_horas = FormularioHoras()
    horas = calcularHorario(request, fecha = fecha)
    formulario_horas = FormularioHoras()
    nueva_salida = Salida()
    categoria_salida = Categoria.objects.get(nombre=categoria)
    nueva_salida.categoria = categoria_salida
    nueva_salida.fecha = fecha
    nueva_salida.descripcion = cajaTexto
    nueva_salida.amigo_id = amigo_id
    nueva_salida.cliente_id = cliente_id
    if request.method == 'POST':
        formulario_datos = FormularioHoras(request.POST)
        if formulario_datos.is_valid():
            nueva_salida.horaInicio = request.POST.get('horaInicio')
            nueva_salida.horaFin = request.POST.get('horaFin')        
            nueva_salida.save()
            return redirect('ProgramarSalida')
        else:
            return render(request, 'programarSalida/escogerHora.html', {'formHoras': formulario_datos, 'horas': horas, 'errores': formulario_datos.errors})
    return render(request, 'programarSalida/escogerHora.html', {'horas': horas, 'formHoras': formulario_horas})

def calcularHorario(request, fecha):
    amigo_id = obtenerAmigoId(request)
    cliente_id = 1  # Reemplaza esto con el id del cliente que quieres filtrar
    horas = DisponibilidadHoras.objects.filter(amigo_id=amigo_id)  
    salidas = Salida.objects.filter(amigo_id=amigo_id, cliente_id=cliente_id, fecha=fecha)
    horas_disponibles = []
    for hora in horas:
        conflicto = False
        for salida in salidas:
            if (salida.horaInicio < hora.horaFin) and (salida.horaFin > hora.horaInicio):
                conflicto = True
                break
        if not conflicto:
            horas_disponibles.append(hora)

    return horas_disponibles

def obtenerAmigoId(request):
    amigo_id = request.GET.get('amigo_id', None)
    if amigo_id is not None:
        return int(amigo_id)
    else:
        return 1  # Reemplaza esto None cuando ya se tenga la opcion de visualizar Perfil de Amigos
def obtenerClienteId():
    return 1  # Reemplaza esto con el id del cliente que quieres asignar
