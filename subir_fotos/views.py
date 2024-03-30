from django.shortcuts import render, redirect
from .models import FotoPerfil

def cargar_fotos_perfil(request):
    if request.method == 'POST':
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist('file-input')
        
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file)
            try:
                profile_photo.save()
            except Exception as e:
                print(e)
        fotos_perfil = FotoPerfil.objects.all() # Definir fotos_perfil antes del bucle
        return render(request, 'subir_fotos/listado.html', {'fotos': fotos_perfil})
    else:
        return render(request, 'subir_fotos/formulario.html') # Renderizar la plantilla del formulario de subida
