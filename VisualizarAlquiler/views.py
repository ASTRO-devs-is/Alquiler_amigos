from django.shortcuts import render
from alquilarAmigo.models import Salida, Amigo, User

# Create your views here.
def visualizarAlquiler(request):
    usuario = User.objects.get(id=request.user.id)
    try:
        usuarioAmigo = Amigo.objects.get(correo=usuario.email)
    except:
        usuarioAmigo = None
    if(usuarioAmigo != None):
        salidas = Salida.objects.filter(amigo_id=usuarioAmigo.id)
        amigoTieneSalida = True
        
    else:
        amigoTieneSalida = False
    
    amigo = {'salidas': salidas, 'tieneSalida': amigoTieneSalida}
    

    return render(request, 'VisualizarAlquiler/visualizarAlquiler.html', amigo)