from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.hashers import check_password
from alquilarAmigo.models import Cliente, Amigo, User

# Create your views here.

def inicio_login(request):
    return render(request, 'index.html')

def login_view(request):
   
    if request.method == 'POST':
        print("Handling POST request!!! estamos aqui estamo aqui")
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            try:
                user = User.objects.get(name_user=email)

                if user.password==password:
                    messages.success(request, 'Login exitoso')
                    return redirect('Inicio')  # Asegúrate de que 'Inicio' sea una vista definida en tus URLconf.
                else:
                    messages.error(request, 'El correo o contraseña son incorrectos, usuario no encontrado')
            except User.DoesNotExist:
                messages.error(request, 'El correo o contraseña son incorrectos, usuario no encontrado')
               
        else:
            print("Errores del formulario:", form.errors)
    return render(request, 'index.html', {'form': form})
