from django.shortcuts import render
from alquilarAmigo.models import Amigo
from subir_fotos.models import FotoPerfil

from django.core.paginator import Paginator

def inicio(request):
    amigos = Amigo.objects.all()

    for amigo in amigos:
        foto_perfil = FotoPerfil.objects.filter(fotos=amigo).first()
        if foto_perfil:
            amigo.foto = foto_perfil.image.url
        else:
            amigo.foto = None

    paginador = Paginator(amigos, 8)  # Dividir la lista de amigos en páginas de 6 amigos cada una
    numPagina = request.GET.get('page')
    pagina = paginador.get_page(numPagina)

    return render(request, 'inicio/inicio.html', {'page_obj': pagina})
