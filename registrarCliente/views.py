from django.shortcuts import render, redirect
from .forms import ClienteForm
from alquilarAmigo.models import Cliente, Direccion

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        #print(form.is_valid())
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
                return render(request, 'registro_cliente.html', {'form': form, 'error_mesage': 'El telefono ya esta registrado'})
            else:
                cliente.save()
                return redirect('Inicio')
            
        #else:
        #    print(form.errors) 
        #    
    else:

        form = ClienteForm()
    return render(request, 'registro_cliente.html', {'form': form})

