from django.shortcuts import render, redirect
from .forms import ClienteForm
from alquilarAmigo.models import Cliente, Direccion, User, Categoria, Interes, User_Categoria, User_Interes
from django.shortcuts import get_object_or_404
from subir_fotos.models import FotoPerfil
from subir_fotos.forms import FotoPerfilForm
from django.contrib import messages
from django.core.exceptions import ValidationError
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.urls import reverse


def editar_datos_cliente123(request, id_usuario):
    cliente = Cliente.objects.get(id=id_usuario)
    form = ClienteForm(instance=cliente)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotos=cliente)
    foto_form = FotoPerfilForm(instance=foto_perfil)
    if not cliente.id:
        return render(request, 'editarPerfilCliente.html', {'error': 'Cliente no encontrado'})
   
    return render(request, 'editarPerfilCliente.html', {'form': form, 'cliente': cliente, 'id_usuario': id_usuario,  'foto_form': foto_form,'foto_perfil': foto_perfil})


def actualizar_datos1234 (request,id_usuario):
        
    cliente = get_object_or_404(Cliente, id=id_usuario)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        #form = ClienteForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            cliente = form.save(commit=False)
            direccion = Direccion.objects.create(
                pais=form.cleaned_data['pais'],
                ciudad=form.cleaned_data['ciudad'],
                localidad=form.cleaned_data['localidad'],
                
            )
            cliente.ubicacion = direccion
            #Verificamos si el telefono existe en la base de datos
            #if Cliente.objects.filter(telefono=telefono).exists():
            if Cliente.objects.exclude(id=id_usuario).filter(telefono=telefono).exists():
                return render(request, 'editarPerfilCliente.html', {'form': form, 'telefonoRepetido': 'Este telefono ya esta registrado'})
            #elif Cliente.objects.filter(correo=direccion.correo).exists():
            #    return render(request, 'editarPerfilCliente.html', {'form': form, 'correoRepetido': 'Este correo ya esta registrado'})
            else:
                cliente.save()
                return redirect('Inicio')
    
    else:

        #form = ClienteForm()
        form = ClienteForm(instance=cliente)
    return render(request, 'editarPerfilCliente.html', {'form': form})
 
def editarCliente(request, id_usuario):
    cliente = get_object_or_404(Cliente, id=id_usuario)
    foto_perfil, created = FotoPerfil.objects.get_or_create(fotosCliente=cliente)
    foto_form = FotoPerfilForm(instance=foto_perfil)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        foto_form = FotoPerfilForm(request.POST, request.FILES, instance=foto_perfil)

        # Validar el formulario amigo manualmente para el campo telefono
        telefono_cambiado = False
        if 'telefono' in form.changed_data:
            telefono_cambiado = True
        print("Estamos en POST")
        print(form.is_valid())
        print(foto_form.is_valid())
        print(form.errors)
        if form.is_valid():

            if telefono_cambiado:
                # Validar teléfono manualmente si ha cambiado
                telefono = form.cleaned_data['telefono']
                if Cliente.objects.filter(telefono=telefono).exclude(id=cliente.id).exists():
                    form.add_error('telefono', 'Este número de teléfono ya está registrado')
            # Si no hay errores, considerar el formulario válido
            if not form.errors and foto_form.is_valid():
                form.save()
                foto_perfil = foto_form.save(commit=False)
                foto_perfil.fotosCliente = cliente
                foto_perfil.save()
                messages.success(request, 'Perfil actualizado con éxito')
                return redirect('Inicio')
        else:
            print("Errores en el formulario:", form.errors)

    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editarPerfilCliente.html', {
        'form': form,
        'foto_form': foto_form,
        'cliente': cliente,
        'foto_perfil': foto_perfil,
        'id_usuario': id_usuario,
    })

#cargar categorias XD actuales del amigo
def loadCategInters(request, id_usuario):
    # Obtener el amigo
    #amigo = get_object_or_404(User, pk=id_usuario)
    cliente = request.user
    print(cliente)

    # Obtener los intereses del amigo
    intereses_amigo = User_Interes.objects.filter(user=cliente, activo_uc=True).values_list('interes__interes', flat=True)
    # Obtener las categorías del amigo
    categorias_amigo = User_Categoria.objects.filter(user=cliente, activo_uc=True).values_list('categoria__nombre', flat=True)

    # Obtener todos los intereses y categorías disponibles
    intereses_disponibles = list(Interes.objects.values_list('interes', flat=True))
    categorias_disponibles = list(Categoria.objects.values_list('nombre', flat=True))

    context = {
        'intereses_amigo': json.dumps(list(intereses_amigo)),
        'categorias_amigo': json.dumps(list(categorias_amigo)),
        'intereses_disponibles': json.dumps(intereses_disponibles),
        'categorias_disponibles': json.dumps(categorias_disponibles),
        'id_usuario': id_usuario
    }

    return render(request, 'editCategInteres.html', context)

#guardar nuevas categorias e intereses de cliente en base de datos
def update_categ_interes(request, id_usuario):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #user = get_object_or_404(User, pk=id_usuario)
            cliente = request.user

            # Limpiar los intereses y categorías actuales del usuario
            User_Interes.objects.filter(user=cliente).delete()
            User_Categoria.objects.filter(user=cliente).delete()

            # Añadir los nuevos intereses
            for interes_name in data.get('interests', []):
                interes = get_object_or_404(Interes, interes=interes_name)
                User_Interes.objects.create(user=cliente, interes=interes)

            # Añadir las nuevas categorías
            for categoria_name in data.get('categories', []):
                categoria = get_object_or_404(Categoria, nombre=categoria_name)
                User_Categoria.objects.create(user=cliente, categoria=categoria)

            # Construir la URL de redirección
            redirect_url = reverse('editarCliente', args=[id_usuario])
            response_data = {
                'status': 'success',
                'message': 'Datos actualizados correctamente',
                'redirect_url': redirect_url  # URL de redirección
            }
            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

