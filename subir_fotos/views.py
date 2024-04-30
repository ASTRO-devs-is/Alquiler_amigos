from django.shortcuts import render, redirect
from .models import FotoPerfil
from alquilarAmigo.models import Amigo, Direccion, Tarifa
from subir_fotos.models import FotoPerfil
from urllib.parse import unquote



def cargar_fotos_perfil(request, nombre, apellido, ciudad, pais, telefono, email, localidad, descripcion, fecha, tarifa, genero):

    
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
        
        for uploaded_file in uploaded_files:
            profile_photo = FotoPerfil(image=uploaded_file, fotos=amigo)
            profile_photo.save()
        return redirect('Inicio')
    else:
        return render(request, 'formulario.html') # Renderizar la plantilla del formulario de subida
    
def cancelar_subir_fotos(request):
    return render(request, 'cancelar.html')

    
    
