from django.shortcuts import render, redirect
from .forms import formularioRegistrarAmigo
from urllib.parse import quote, unquote
from alquilarAmigo.models import DisponibilidadHoras, Amigo,User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
def registrarAmigo(request):
    formulario = formularioRegistrarAmigo()
    print('aquiesta')
    print(formulario['contrasena'])
    if request.method == 'POST':
        form = formularioRegistrarAmigo(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
           # Convertir la fecha a un formato serializable
            fecha = form.cleaned_data['fecha'].isoformat()

            # Guardar los datos del formulario en la sesión
            request.session['datos_registro'] = {
                'nombre': form.cleaned_data['nombre'],
                'apellido': form.cleaned_data['apellido'],
                'ciudad': form.cleaned_data['ciudad'],
                'pais': form.cleaned_data['pais'],
                'telefono': form.cleaned_data['telefono'],
                'email': form.cleaned_data['email'],
                'localidad': form.cleaned_data['localidad'],
                'descripcion': quote(form.cleaned_data['descripcion']),
                'fecha': fecha,
                'tarifa': form.cleaned_data['tarifa'],
                'genero': form.cleaned_data['genero'],
                'contrasena': form.cleaned_data['contrasena']
            }

            return redirect('subir_foto')
        return render(request, "registrarAmigo/registrarAmigo.html", {'form': form, 'errores': form.errors})
    return render(request, "registrarAmigo/registrarAmigo.html", {'form': formulario})

def aniadirHoras(request):
    horas = ["Desde {:02d}:00 Hasta {:02d}:00".format(h, h+1) for h in range(8, 22)]
    usuario = User.objects.get(id=request.user.id)
    usuarioAmigo = Amigo.objects.get(correo=usuario.email)
  
    if request.method == 'POST':
        horasParaGuardar = DisponibilidadHoras
        horasParaGuardar.objects.filter(amigo=usuarioAmigo).delete()
        horarios_seleccionados = []
        #print(horas)
        for i in range(1, len(horas)+1):
            horario = request.POST.get('horario_seleccionado_{}'.format(i))
            #print(horario)
            if horario:
                horarios_seleccionados.append(horario)
        #print(horarios_seleccionados)
        # Aquí puedes procesar los horarios seleccionados
        for horario in horarios_seleccionados:
            horaInicio, horaFin = horario.split(" Hasta ")
            horaInicio = horaInicio.replace("Desde ", "")
            horasParaGuardar.objects.create(amigo=usuarioAmigo, horaInicio=horaInicio, horaFin=horaFin)
            #print("HOLA",horaInicio, horaFin, usuarioAmigo,"FINHOLA")
            
        return redirect('Inicio')
    return render(request, "aniadirHoras/aniadirHoras.html", {'horas': horas})

def cancelar_aniadir_horas(request):
    return render(request, 'aniadirHoras/cancelar.html')

def politicadeprivacidad(request):
    return render(request, 'legal/politica.html')

def terminosycondiciones(request):
    return render(request, 'legal/terminos.html')