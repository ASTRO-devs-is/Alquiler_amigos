from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            #Verificamos si el telefono existe en la base de datos
            if Cliente.objects.filter(telefono=telefono).exists():
                return render(request, 'registro_cliente.html', {'form': form, 'error_mesage': 'El telefono ya esta registrado'})
            else:
                cliente = form.save()
            return redirect('exito_registro')
    else:
        form = ClienteForm()
    return render(request, 'registro_cliente.html', {'form': form})

def exito_registro(request):
    return render(request, 'exito_registro.html')
