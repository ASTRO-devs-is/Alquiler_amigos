from django.db import models

class FotoPerfil(models.Model):
    image = models.ImageField(upload_to='fotos_perfil/')  # Path to store images

    def __str__(self):
        return str(self.image)
