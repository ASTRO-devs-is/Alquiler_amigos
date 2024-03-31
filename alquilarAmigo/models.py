from django.db import models
from subir_fotos.models import FotoPerfil
# Create your models here.
class Salida(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    amigo = models.ForeignKey('Amigo', on_delete=models.CASCADE)
    cajaT = models.TextField()
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (self.categoria.nombre + ' - ' + self.cliente.nombre + ' - ' + self.amigo.nombre + ' - ' + 
                self.fecha.strftime('%d/%m/%Y') + ' - ' + self.horaInicio.strftime('%H:%M') + ' - ' +
                self.horaFin.strftime('%H:%M'))
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class Amigo(models.Model):

    nombre = models.CharField(max_length=50, blank = False)
    apellido = models.CharField(max_length=50, blank = False)
    ciudad = models.CharField(max_length=50, blank = False)
    pais = models.CharField(max_length=50, blank = False)
    telefono = models.CharField(max_length=8)
    localidad = models.CharField(max_length=50, blank = False)
    descripcion = models.TextField(max_length=500, blank = False)
    fecha = models.DateField(blank = False)
    tarifa = models.IntegerField(blank = False)
    correo = models.EmailField(blank = False)
    disponibilidad = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    fotos = models.ManyToManyField(FotoPerfil, blank=True) 
    def __str__(self):
        return self.nombre
    
class DisponibilidadDias(models.Model):
    dias = models.CharField(max_length=10)
    amigo = models.ForeignKey('Amigo', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.dias

class DisponibilidadHoras(models.Model):
    amigo = models.ForeignKey('Amigo', on_delete=models.CASCADE)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.horaInicio.strftime('%H:%M') + ' - ' + self.horaFin.strftime('%H:%M')
    
class Tarifa(models.Model):
    tarifa = models.IntegerField()