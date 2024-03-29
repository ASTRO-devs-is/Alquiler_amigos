from django.shortcuts import render
from .forms import formularioProgramarCita
import datetime
# Create your views here.

def programarSalida(request):
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
            return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_datos, 'errores': formulario_datos.errors})
            
                
    return render(request, 'programarSalida/programarSalida.html', {'formSalida': formulario_programarSalida})