from django.shortcuts import render


# Create your views here.
def crearCuenta(request):
    return render(request, 'crearCuenta/crearCuenta.html')

