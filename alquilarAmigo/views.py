from django.shortcuts import render
from .forms import formularioProgramarCita
# Create your views here.

def programarSalida(request):
    formulario_categoria = formularioProgramarCita()
    if request.method == 'POST':
        #formulario_salida = formularioProgramarCita(request.POST)#metemos la informacion de los cuadros al formulario
        
        categorias = request.POST.get('categorias')
        fecha = request.POST.get('fecha')
        cajaTexto = request.POST.get('cajaTexto')
        horaInicio = request.POST.get('horaInicio')
        horaFin = request.POST.get('horaFin')
        datos = {'categorias': categorias, 'fecha': fecha, 'cajaTexto': cajaTexto, 'horaInicio': horaInicio, 'horaFin': horaFin}
        return render(request, "programarSalida/respuesta.html", {'datos': datos})
                
    return render(request, 'programarSalida/programarSalida.html', {'formCateg': formulario_categoria})