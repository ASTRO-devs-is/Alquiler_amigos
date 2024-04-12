from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo, Direccion, Tarifa
from subir_fotos.models import FotoPerfil
import json
import os
from django.core.files.storage import default_storage

def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa, genero):

    datos = []
    if request.method == 'POST':
       
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
      
        for uploaded_file in uploaded_files:
            file_name = default_storage.save('tmp/' + uploaded_file.name, uploaded_file)
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            datos.append({'nombre': nombre, 'apellido': apellido, 'ciudad': ciudad, 'pais': pais, 'telefono': telefono,
                        'email': email, 'localidad': localidad, 'descripcion': descripcion, 'fecha': fecha, 'tarifa': tarifa,
                        'genero': genero, 'foto': file_name})
            
        #datos_json = json.dumps(datos)
        request.session['datos'] = datos
        #return redirect('exito', datos=datos_json)
        return redirect('exito')
    else:
        return render(request, 'formulario.html') # Renderizar la plantilla del formulario de subida
    
#def exito(request, datos=None):
def exito(request):

    #datos_nuevos = json.loads(datos)
    datos_nuevos = request.session.get('datos', [])
    datosA = datos_nuevos[0]
    datos_cuenta = {
        'nombre': datosA['nombre'],
        'apellido': datosA['apellido'],
        'telefono': datosA['telefono'],
        'correo': datosA['email'],
        'descripcion': datosA['descripcion'],
        'fecha_nacimiento': datosA['fecha'],
        'ubicacion': {
            'ciudad': datosA['ciudad'],
            'pais': datosA['pais'],
            'localidad': datosA['localidad'],
        },
        'tarifa': datosA['tarifa'],
    }
    if request.method == 'POST':
        datos = datos_nuevos[0]
        tarifa = Tarifa.objects.get(tarifa=datos['tarifa'])
        direccion = Direccion(ciudad=datos['ciudad'], pais=datos['pais'], localidad=datos['localidad'])
        direccion.save()
        id_ubicacion = direccion.id
        amigo = Amigo(nombre=datos['nombre'], apellido=datos['apellido'], telefono=datos['telefono'], 
                    ubicacion_id= id_ubicacion, correo=datos['email'],
                    descripcion=datos['descripcion'], fecha_nacimiento=datos['fecha'], id_tarifa=tarifa, genero = datos['genero'])
        amigo.save()
        for dato in datos_nuevos:
            foto = dato['foto']
            profile_photo = FotoPerfil(image=foto, fotos=amigo)
            profile_photo.save()
        del request.session['datos']
        return redirect('Inicio')
    return render(request, 'exito.html', {'datos_cuenta': datos_cuenta})

def cancelar_subir_fotos(request, datos=None):
    return render(request, 'cancelar.html')

    
    
