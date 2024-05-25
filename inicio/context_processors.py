from alquilarAmigo.models import User, Amigo, Cliente

def usuarioLog(request):
    amigo = {'esAmigo': False}
    if request.user.is_authenticated:
        usuario = User.objects.get(id=request.user.id)
        try:
            usuarioAmigo = Amigo.objects.get(correo=usuario.email)
            if usuarioAmigo is not None:
                amigo['amigo'] = usuarioAmigo
                amigo['esAmigo'] = True
        except Amigo.DoesNotExist:
            pass

        try:
            usuarioCliente = Cliente.objects.get(correo=usuario.email)
            if usuarioCliente is not None:
                amigo['cliente'] = usuarioCliente
        except Cliente.DoesNotExist:
            pass
    else:
        amigo = None

    return {'usuario': amigo}