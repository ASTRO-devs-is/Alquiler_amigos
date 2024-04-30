from django.db import models

class Interes(models.Model):
    interes = models.CharField(max_length= 255)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    categoria = models.CharField(max_length= 255)

    def __str__(self):
        return self.nombre

class User_Categoria (models.Model):
    user = models.ForeignKey('User', on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    activo_uc = models.BooleanField(default=True)

    class Meta: 
        unique_together = ('user','categoria')    
    
class User_Interes (models.Model):
    user = models.ForeignKey('User', on_delete= models.CASCADE)
    interes = models.ForeignKey(Interes, on_delete= models.CASCADE)
    activo_uc = models.BooleanField(default=True)

    class Meta: 
        unique_together = ('user','interes')

