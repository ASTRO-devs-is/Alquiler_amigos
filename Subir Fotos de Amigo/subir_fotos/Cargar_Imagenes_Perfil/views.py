from django.shortcuts import render, redirect
from .models import FotoPerfil

def cargar_fotos_perfil(request):
    if request.method == 'POST':
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
        images_cargadas = [];
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file)
            profile_photo.save()
            images_cargadas.append(profile_photo.image.url)

        #Pasamos las URLs de las fotos cargadas al contexto
        contex = {'imagenes_cargadas': images_cargadas}
        return render(request, 'subir_fotos/exito.html', contex)
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida

def exito(request):
    return render(request, 'subir_fotos/exito.html')