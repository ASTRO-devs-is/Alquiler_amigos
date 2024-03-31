from django.db import models
from alquilarAmigo.models import Amigo
# Create your models here.
class FotoPerfil(models.Model):

    image = models.ImageField(upload_to='fotos_perfil/')  # Path to store images
    fotos = models.ForeignKey(Amigo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Foto de perfil: {self.image.name}"
