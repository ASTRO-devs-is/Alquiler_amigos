from django.db import models

# Create your models here.
class FotoPerfil(models.Model):
    image = models.ImageField(upload_to='fotos_perfil/')  # Path to store images

    def __str__(self):
        return f"Foto de perfil: {self.image.name}"
