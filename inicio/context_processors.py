from alquilarAmigo.models import User, Amigo

def usuarioLog(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
        try:
            usuarioAmigo = Amigo.objects.get(correo=usuario.email)
        except:
            usuarioAmigo = None
        if(usuarioAmigo != None):
            amigo = {
                'nombre': usuarioAmigo.nombre,
                'esAmigo': True,
            }
        else:
            amigo = {
                'esAmigo': False,
            }
        
    else:
        amigo = None

    return {'usuario': amigo}