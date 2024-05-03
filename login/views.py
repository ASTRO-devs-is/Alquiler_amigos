from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from alquilarAmigo.models import Cliente, Amigo, User

# Create your views here.

def inicio_login(request):
    return render(request, 'index.html')

def login_view(request):
   
    if request.method == 'POST':
       
        form = LoginForm(request.POST)
        if form.is_valid():

            email_log = form.cleaned_data.get('email')
            contra = form.cleaned_data.get('password')
            if email_log.endswith('@gmail.com') or email_log.endswith('@hotmail.com'):
                try:
                   
                    user = authenticate(email=email_log, password=contra)
                    
                    if user is not None:
                        login(request, user)  # Inicia sesión con el usuario
                        messages.success(request, 'Login exitoso')
                        return redirect('Inicio')  # Asegúrate de que 'Inicio' sea una vista definida en tus URLconf.
                    else:
                        messages.error(request, 'El correo o contraseña son incorrectos, usuario no encontrado')
                except User.DoesNotExist:
                    messages.error(request, 'El correo o contraseña son incorrectos, usuario no encontrado')
            else: 
                 messages.error(request, 'Registrate con correo válido @gmail o @hotmail')


        else:
            print("Errores del formulario:", form.errors)
    return render(request, 'index.html', {'form': form})
