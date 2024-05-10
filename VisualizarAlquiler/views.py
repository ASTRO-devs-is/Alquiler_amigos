from django.shortcuts import render
from alquilarAmigo.models import Salida, Amigo, User
from subir_fotos.models import FotoPerfil

# Create your views here.
def visualizarAlquiler(request):
    usuarioA = User.objects.get(id=request.user.id)
    
    try:
        usuarioAmigo = Amigo.objects.get(correo=usuarioA.email)
    except:
        usuarioAmigo = None
    if(usuarioAmigo != None):
        salidas = Salida.objects.filter(amigo_id=usuarioAmigo.id)
        amigoTieneSalida = True
        salidas_con_fotos = [{'salida': salida, 'foto': FotoPerfil.objects.filter(fotosCliente__id=salida.cliente.id).first()} for salida in salidas]
    else:
        amigoTieneSalida = False
    
    #print(salidas)
    print(salidas_con_fotos)
    
    return render(request, 'VisualizarAlquiler/visualizarAlquiler.html', {'contexto': {'salidas_con_fotos': salidas_con_fotos, 'tieneSalida': amigoTieneSalida}})