from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo
from subir_fotos.models import FotoPerfil

def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa):
    if request.method == 'POST':
        amigo = Amigo(nombre=nombre, apellido=apellido, ciudad=ciudad, pais=pais, telefono=telefono, correo=email, localidad=localidad, descripcion=descripcion, fecha=fecha, tarifa=tarifa)
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
        amigo.save()
        return redirect('Inicio')
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida
