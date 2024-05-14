from django.shortcuts import render, redirect
from .forms import ClienteForm
from alquilarAmigo.models import Cliente, Direccion, User
from django.shortcuts import get_object_or_404

def editar_datos_cliente(request, id_usuario):
    cliente = Cliente.objects.get(id=id_usuario)
    form = ClienteForm(instance=cliente)
   
    return render(request, 'editarPerfilCliente.html', {'form': form, 'cliente': cliente, 'id_usuario': id_usuario})


def actualizar_datos (request,id_usuario):
        
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
 
