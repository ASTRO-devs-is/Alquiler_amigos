from django.shortcuts import render
from alquilarAmigo.models import Salida, Amigo, User
from subir_fotos.models import FotoPerfil
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
    
    return render(request, 'VisualizarAlquiler/visualizarAlquiler.html', {'contexto': {'salidas_con_fotos': salidas_con_fotos, 'tieneSalida': amigoTieneSalida}})


@csrf_exempt
def cambiar_estado_salida(request):
    print("primera prueba")
    if request.method == 'POST':
        print("segunda prueba")
        id = request.POST.get('id')
        estado = request.POST.get('estado')

        if id and estado:
            try:
                salida = Salida.objects.get(id=id)
                salida.estado_salida = estado
                salida.save()
                print(estado)
                print("Cuadrta prueba")
                return JsonResponse({'success': True})
                
            except Salida.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Salida no encontrada'})
        else:
            return JsonResponse({'success': False, 'error': 'ID o estado no proporcionado'})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'})