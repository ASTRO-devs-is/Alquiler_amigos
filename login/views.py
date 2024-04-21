from django.shortcuts import render

# Create your views here.

def inicio_login(request):
    return render(request, 'index.html')