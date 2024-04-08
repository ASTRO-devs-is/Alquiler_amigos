from django.shortcuts import render, redirect
from .models import FotoPerfil
from django.http import JsonResponse

def cargar_fotos_perfil(request):
    if request.method == 'POST':
        # Obtener archivos subidos
        uploaded_files = request.FILES.getlist("file-input")
        imagenes_cargadas = []
        for uploaded_file in uploaded_files:
            # Crear un nuevo objeto ProfilePhoto y guardar la imagen
            profile_photo = FotoPerfil(image=uploaded_file)
            profile_photo.save()
            imagenes_cargadas.append(profile_photo.image.url)
        return JsonResponse({'success': True})
    else:
        return render(request, 'formulario.html') # Renderizar la plantilla del formulario de subida
        
def exito(request):
    context ={'imagenes_cargadas': FotoPerfil.objects.values_list('image', flat=True)}
    return render(request, 'exito.html', context)