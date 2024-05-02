from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo, Direccion, Tarifa,User
from subir_fotos.models import FotoPerfil
from datetime import date
from urllib.parse import unquote
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa, genero,contraseña):
#def cargar_fotos_perfil(request):
    
    if request.method == 'POST':
        
        # Obtener archivos subidos
        descripcion_decodificada = unquote(descripcion)
        uploaded_files = request.FILES.getlist('file-input')
        tarifa = Tarifa.objects.get(tarifa=tarifa)
        direccion = Direccion(ciudad=ciudad, pais=pais, localidad=localidad)
        direccion.save()
        id_ubicacion = direccion.id
        
        amigo = Amigo(nombre=nombre, apellido=apellido, telefono=telefono, 
                    ubicacion_id= id_ubicacion, correo=email,
                    descripcion=descripcion_decodificada, fecha_nacimiento=fecha, id_tarifa=tarifa, genero = genero)
        amigo.save()
        
        user = User.objects.create_user(
                    username=email,
                    password=contraseña,
                    email=email
                )
        print ('Contraseña con hash')
        print(user.password)
        user.save()

        
        for uploaded_file in uploaded_files:
            profile_photo = FotoPerfil(image=uploaded_file, fotos=amigo)
            profile_photo.save()
        return redirect('Inicio')
    else:
        return render(request, 'formulario.html') # Renderizar la plantilla del formulario de subida
"""
def cargar_fotos_perfil(request):
    if request.method == 'POST':
        registro_data = request.session.get('registro_data')
        if not registro_data:
            # Redirige de nuevo al formulario si no hay datos o la sesión ha expirado
            return redirect('registroAmigo')
        
        # Convierte el string de la fecha de nuevo a un objeto date
        if 'fecha' in registro_data and registro_data['fecha']:
            registro_data['fecha'] = date.fromisoformat(registro_data['fecha'])


        # Procesar los datos obtenidos de la sesión
        tarifa = Tarifa.objects.get(tarifa=registro_data['tarifa'])
        direccion = Direccion(ciudad=registro_data['ciudad'], pais=registro_data['pais'], localidad=registro_data['localidad'])
        direccion.save()
        
        amigo = Amigo(
            nombre=registro_data['nombre'], apellido=registro_data['apellido'],
            telefono=registro_data['telefono'], ubicacion=direccion,
            correo=registro_data['email'], descripcion=registro_data['descripcion'],
            fecha_nacimiento=registro_data['fecha'], id_tarifa=tarifa, genero=registro_data['genero']
        )
        amigo.save()

        User = get_user_model()
        user = User.objects.create_user(
            username=registro_data['email'],
            password=registro_data['contraseña'],
            email=registro_data['email']
        )
        user.save()

        uploaded_files = request.FILES.getlist('file-input')
        for uploaded_file in uploaded_files:
            profile_photo = FotoPerfil(image=uploaded_file, fotos=amigo)
            profile_photo.save()

        return redirect('Inicio')
    else:
        return render(request, 'formulario.html')
  """    
def cancelar_subir_fotos(request):
    return render(request, 'cancelar.html')

    
    
