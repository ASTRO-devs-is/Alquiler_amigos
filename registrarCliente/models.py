from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    descripcion = models.TextField()
    aviso_legal_aceptado = models.BooleanField()
    terminos_condiciones_aceptados = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"