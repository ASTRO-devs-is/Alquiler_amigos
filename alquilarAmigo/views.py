from django.shortcuts import render

# Create your views here.
def programarSalida(request):
    return render(request, 'programarSalida/programarSalida.html')