from django.shortcuts import render
from alquilarAmigo.models import Salida, Amigo, User
from subir_fotos.models import FotoPerfil
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

# Create your views here.
def visualizarAlquiler(request):
    
    usuarioA = User.objects.get(id=request.user.id)
    
    try:
        usuarioAmigo = Amigo.objects.get(correo=usuarioA.email)
    except:
        usuarioAmigo = None
    if(usuarioAmigo != None):
        salidas = Salida.objects.filter(amigo_id=usuarioAmigo.id).order_by('-created')
        if len(salidas) > 5:
            
            paginator = Paginator(salidas, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            page_obj = salidas
        amigoTieneSalida = True
        salidas_con_fotos = [{'salida': salida, 'foto': FotoPerfil.objects.filter(fotosCliente__id=salida.cliente.id).first()} for salida in page_obj]
    else:
        amigoTieneSalida = False
    
    return render(request, 'visualizarAlquiler/visualizarAlquiler.html', 
                    {'contexto': {'page_obj': page_obj, 'salidas_con_fotos': salidas_con_fotos, 'tieneSalida': amigoTieneSalida}})


@csrf_exempt
def cambiar_estado_salida(request):
    #print("primera prueba")
    if request.method == 'POST':
        #print("segunda prueba")
        id = request.POST.get('id')
        estado = request.POST.get('estado')

        if id and estado:
            try:
                salida = Salida.objects.get(id=id)
                salida.estado_salida = estado
                salida.save()
                #print(estado)
                #print("Cuadrta prueba")
                return JsonResponse({'success': True})
                
            except Salida.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Salida no encontrada'})
        else:
            return JsonResponse({'success': False, 'error': 'ID o estado no proporcionado'})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'})
    
def historial(request):
    usuarioA = User.objects.get(id=request.user.id)
    
    try:
        usuarioAmigo = Amigo.objects.get(correo=usuarioA.email)
    except:
        usuarioAmigo = None
    if(usuarioAmigo != None):
        salidas = Salida.objects.filter(amigo_id=usuarioAmigo.id).order_by('-updated')
        amigoTieneSalida = True
        salidasNoPendientes = salidas.exclude(estado_salida='Pendiente')
        #print(len(salidasNoPendientes))
        if len(salidasNoPendientes) > 5:
            
            paginator = Paginator(salidas, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            page_obj = salidas
        salidas_con_fotos = [{'salida': salida, 'foto': FotoPerfil.objects.filter(fotosCliente__id=salida.cliente.id).first()} for salida in page_obj]
    else:
        amigoTieneSalida = False
    
    return render(request, 'visualizarAlquiler/historial.html', {'contexto': {'page_obj': page_obj,'salidas_con_fotos': salidas_con_fotos, 'tieneSalida': amigoTieneSalida}})
