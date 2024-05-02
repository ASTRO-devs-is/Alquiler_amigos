from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo, Direccion, Tarifa,User
from subir_fotos.models import FotoPerfil
from urllib.parse import unquote
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



def cargar_fotos_perfil(request):
    if request.method == 'POST':
        # Recuperar los datos del formulario de la sesión
        datos_registro = request.session.get('datos_registro')
        if not datos_registro:
            # Redirigir o manejar el caso en que los datos no estén disponibles en la sesión
            pass

        # Obtener archivos subidos
        descripcion_decodificada = unquote(datos_registro['descripcion'])
        uploaded_files = request.FILES.getlist('file-input')
        tarifa = Tarifa.objects.get(tarifa=datos_registro['tarifa'])
        direccion = Direccion(ciudad=datos_registro['ciudad'], pais=datos_registro['pais'], localidad=datos_registro['localidad'])
        direccion.save()
        id_ubicacion = direccion.id
        
        amigo = Amigo(nombre=datos_registro['nombre'], apellido=datos_registro['apellido'], telefono=datos_registro['telefono'], 
                    ubicacion_id= id_ubicacion, correo=datos_registro['email'],
                    descripcion=descripcion_decodificada, fecha_nacimiento=datos_registro['fecha'], id_tarifa=tarifa, genero = datos_registro['genero'])
        amigo.save()
        
        user = User.objects.create_user(
                    username=datos_registro['email'],
                    password=datos_registro['contrasena'],
                    email=datos_registro['email']
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
    
def cancelar_subir_fotos(request):
    return render(request, 'cancelar.html')

    
    
