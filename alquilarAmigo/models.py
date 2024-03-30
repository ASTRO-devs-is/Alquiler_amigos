from django.db import models

# Create your models here.
class Salida(models.Model):
    categoria = models.CharField(max_length=50)
    cajaT = models.TextField()
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    def __str__(self):
        return self.categorias