from django.shortcuts import render, redirect
from .models import FotoPerfil

def cargar_fotos_perfil(request):
    if request.method == 'POST':
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file)
            profile_photo.save()
        return redirect('exito')  # Redirigir a una página de éxito (opcional)
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida
