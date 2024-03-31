from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo

def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa):
    if request.method == 'POST':
        amigo = Amigo(nombre=nombre, apellido=apellido, ciudad=ciudad, pais=pais, telefono=telefono, correo=email, localidad=localidad, descripcion=descripcion, fecha=fecha, tarifa=tarifa)
        amigo.save()
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
        
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file)
            try:
                profile_photo.save()
                amigo.fotos.add(profile_photo)
            except Exception as e:
                print(e)
        amigo.save()
        fotos_perfil = FotoPerfil.objects.all() # Definir fotos_perfil antes del bucle
        return redirect('Inicio')
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida
