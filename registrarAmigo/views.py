from django.shortcuts import render, redirect
from .forms import formularioRegistrarAmigo
from urllib.parse import quote, unquote
from alquilarAmigo.models import DisponibilidadHoras, Amigo


# Create your views here.
def registrarAmigo(request):
    formulario = formularioRegistrarAmigo()
    if request.method == 'POST':
        form = formularioRegistrarAmigo(request.POST)
        if form.is_valid():
            nombre =request.POST['nombre']
            apellido = request.POST['apellido']
            ciudad = request.POST['ciudad']
            pais = request.POST['pais']
            telefono = request.POST['telefono']
            email = request.POST['email']
            localidad = request.POST['localidad']
            tarifa = request.POST['tarifa']
            genero = request.POST['genero']  #agregar campo genero y obtenerlo del formulario pero en tipo numerico
            descripcion = request.POST['descripcion']
            fecha = request.POST['fecha']
            descripcion_codificada = quote(descripcion)

            

            return redirect('subir_foto', nombre=nombre, apellido=apellido, ciudad=ciudad,
                                        pais=pais, telefono=telefono, email=email, localidad=localidad,
                                        descripcion=descripcion_codificada, fecha=fecha,tarifa=tarifa, genero = genero)
        return render(request, "registrarAmigo/registrarAmigo.html", {'form': form, 'errores': form.errors})
    return render(request, "registrarAmigo/registrarAmigo.html", {'form': formulario})

def aniadirHoras(request):
    horas = ["Desde {:02d}:00 Hasta {:02d}:00".format(h, h+1) for h in range(8, 22)]
    usuarioAmigo = Amigo.objects.get(id=request.user.id)
    #print (usuarioAmigo)
    if request.method == 'POST':
        horasParaGuardar = DisponibilidadHoras
        horarios_seleccionados = []
        #print(horas)
        for i in range(1, len(horas)+1):
            horario = request.POST.get('horario_seleccionado_{}'.format(i))
            #print(horario)
            if horario:
                horarios_seleccionados.append(horario)
        #print(horarios_seleccionados)
        # Aquí puedes procesar los horarios seleccionados
        for horario in horarios_seleccionados:
            horaInicio, horaFin = horario.split(" Hasta ")
            horaInicio = horaInicio.replace("Desde ", "")
            horasParaGuardar.objects.create(amigo=usuarioAmigo, horaInicio=horaInicio, horaFin=horaFin)
            #print("HOLA",horaInicio, horaFin, usuarioAmigo,"FINHOLA")
            
        return redirect('Inicio')
    return render(request, "aniadirHoras/aniadirHoras.html", {'horas': horas})

def cancelar_aniadir_horas(request):
    return render(request, 'aniadirHoras/cancelar.html')