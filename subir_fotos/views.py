from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo, Direccion, Tarifa
from subir_fotos.models import FotoPerfil

def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa, genero):
    if request.method == 'POST':
        tarifa = Tarifa.objects.get(tarifa=tarifa)
        direccion = Direccion(ciudad=ciudad, pais=pais, localidad=localidad)
        direccion.save()
        id_ubicacion = direccion.id
        amigo = Amigo(nombre=nombre, apellido=apellido, telefono=telefono, ubicacion_id= id_ubicacion, correo=email,
                    descripcion=descripcion, fecha_nacimiento=fecha, id_tarifa=tarifa, genero = genero)
        amigo.save()
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
        
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file, fotos=amigo)
            try:
                profile_photo.save()
            except Exception as e:
                print(e)
        #amigo.save()
        return redirect('Inicio')
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida
