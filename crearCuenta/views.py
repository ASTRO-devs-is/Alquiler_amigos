from django.shortcuts import render


# Create your views here.
def registrarseComo(request):
    return render(request, 'crearCuenta/crearCuenta.html')