from django.shortcuts import render, redirect
from .forms import ClienteForm
from alquilarAmigo.models import Cliente, Direccion, User
from subir_fotos.models import FotoPerfil
from django.contrib.auth.hashers import make_password

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            cliente = form.save(commit=False)
            direccion = Direccion.objects.create(
                pais=form.cleaned_data['pais'],
                ciudad=form.cleaned_data['ciudad'],
                localidad=form.cleaned_data['localidad']
            )
            cliente.ubicacion = direccion
            #Verificamos si el telefono existe en la base de datos
            if Cliente.objects.filter(telefono=telefono).exists():
                return render(request, 'registro_cliente.html', {'form': form, 'telefonoRepetido': 'Este telefono ya esta registrado'})
            elif Cliente.objects.filter(correo=form.cleaned_data['correo']).exists():
                return render(request, 'registro_cliente.html', {'form': form, 'correoRepetido': 'Este correo ya esta registrado'})
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['correo'],
                    password=form.cleaned_data['contrasena'],
                    email=form.cleaned_data['correo']
                )
                user.password = make_password(form.cleaned_data['contrasena'])
                user.save()
                cliente.save()
                return redirect('fotoCliente', idCliente=cliente.id)
            
        else:
            print(form.errors) 
            
    else:

        form = ClienteForm()
    return render(request, 'registro_cliente.html', {'form': form})

def cargar_fotos_perfil(request, idCliente):
    if request.method == 'POST':
        # Recuperar los datos del formulario de la sesión
        cliente = Cliente.objects.get(id = idCliente)
        uploaded_files = request.FILES.getlist('file-input')
        for uploaded_file in uploaded_files:
            profile_photo = FotoPerfil(image=uploaded_file, fotosCliente = cliente)
            profile_photo.save()
        return redirect('Inicio')
    else:
        return render(request, 'formulario.html') # Renderizar la plantilla del formulario de subida
