from django.shortcuts import render

# Create your views here.
def visualizarAlquiler(request):
    return render(request, 'VisualizarAlquiler/visualizarAlquiler.html')