from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Salida(models.Model):
    categoria_salida = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    amigo = models.ForeignKey('Amigo', on_delete=models.CASCADE)
    descripcion_salida = models.TextField()
    fecha_salida = models.DateField()
    hora_inicio_salida = models.TimeField()
    hora_fin_salida = models.TimeField()
    cita_realizada = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (self.categoria_salida.nombre + ' - Cliente: ' + self.cliente.nombre + ' - Amigo: ' + self.amigo.nombre + ' - ' + 
                self.fecha_salida.strftime('%d/%m/%Y') + ' - ' + self.hora_inicio_salida.strftime('%H:%M') + ' - ' +
                self.hora_fin_salida.strftime('%H:%M'))
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    contrasena = models.CharField(max_length=128)
    telefono = models.CharField(max_length=8, blank=True)
    ubicacion = models.ForeignKey("Direccion", on_delete=models.PROTECT)
    correo = models.EmailField(blank=False, unique=True) 
    fecha_nacimiento = models.DateField(blank = False)
    descripcion = models.TextField(max_length=500, blank = False)
    genero = models.IntegerField(blank = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

class Amigo(models.Model):

    nombre = models.CharField(max_length=50, blank = False)
    apellido = models.CharField(max_length=50, blank = False)
    ubicacion = models.ForeignKey("Direccion", on_delete=models.PROTECT)
    telefono = models.CharField(max_length=8, blank=True)
    descripcion = models.TextField(max_length=500, blank = False)
    fecha_nacimiento = models.DateField(blank = False)
    id_tarifa= models.ForeignKey("Tarifa", on_delete= models.CASCADE)
    correo = models.EmailField(blank=False, unique=True) 
    disponibilidad = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    genero = models.IntegerField(blank = False)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Pais: {self.ubicacion.pais} -correo: {self.correo}"
    @classmethod
    def registrar_amigo(cls, nombre, apellidos, ubicacion, telefono, descripcion, fecha_nacimiento, tarifa, correo, genero):
    
        nuevo_amigo = cls(nombre=nombre, apellido=apellidos, ubicacion=ubicacion,telefono=telefono, descripcion=descripcion,
                        fecha_nacimiento=fecha_nacimiento, id_tarifa= tarifa,correo=correo, gerero=genero)
        nuevo_amigo.save()
        return nuevo_amigo
    

    @classmethod
    def telefono_duplicado(cls, telefono):
        # Verificar si el número de teléfono ya existe en la base de datos
        return cls.objects.filter(telefono=telefono).exists()
    
    @classmethod
    def correo_duplicado(cls, correo):
        # Verificar si el correo electrónico ya existe en la base de datos
        return cls.objects.filter(correo=correo).exists()
    
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


class User (models.Model):
    name_user = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128)
    activado = models.BooleanField(default = True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Nombre: {self.name_user} - Activo: {self.activado}"

    
    @classmethod
    def get_id_user(cls, nombre):
        try:
            user = cls.objects.get(name_user=nombre)
            return user.name_user
        except cls.DoesNotExist:
            return None


class Rol (models.Model):
    rol = models.CharField(max_length=255)

    def __str__(self):
        return self.rol
    
class Funcion(models.Model):
    funcion = models.CharField(max_length=255)

    def __srt__(self):
        return self.funcion

class User_Rol(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    activo_ur = models.BooleanField(default=True)
    fecha_desde = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'rol')

class ROl_Funcion(models.Model):
    rol= models.ForeignKey('Rol', on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    activo_rf = models.BooleanField(default=True)

    class Meta:
        unique_together= ('rol', 'funcion')

    
class Interes(models.Model):
    interes = models.CharField(max_length= 255)

    def __srt__(self):
        return self.interes
    
class User_Categoria (models.Model):
    user = models.ForeignKey('User', on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    activo_uc = models.BooleanField(default=True)

    class Meta: 
        unique_together = ('user','categoria')

class Categoria_Interes(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    interes = models.ForeignKey('Interes', on_delete=models.CASCADE)
    activo_ci= models.BooleanField(default= True)

    class Meta:
        unique_together= ('categoria', 'interes')

class Idioma (models.Model):
    idioma = models.CharField(max_length=255)
    def __srt__(self):
        return self.idioma
    
class User_Idioma(models.Model):
    user = models.ForeignKey('User', on_delete= models.CASCADE)
    idioma =models.ForeignKey('Idioma', on_delete=models.CASCADE)
    activo_ui= models.BooleanField(default= True)

    class Meta:
        unique_together=('user', 'idioma')

class Reporte (models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    reporte= models.CharField(max_length= 500)
    fecha_reporte= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reporte {self.id_reporte} - Usuario: {self.user.name_user}"
    
class Post (models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    descripcion_post =models.CharField(max_length=500)
    fecha_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reporte {self.id_post} - Usuario: {self.user.name_user}"
    
class Calificacion (models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    puntaje = models.IntegerField()
    fecha_calificacion= models.DateField(auto_now_add=True)
    
    
class Tipo_Archivo(models.Model):
    tipo_archivo = models.CharField(max_length = 50)

    def __srt__(self):
        return self.tipo_archivo
    
class Archivo(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    tipo_archivo = models.ForeignKey(Tipo_Archivo,on_delete=models.CASCADE)
    name_archivo = models.CharField(max_length = 255)
    archivo= models.BinaryField()
    fehca_archivo = models.DateField(auto_now_add=True)

    def __srt__(self):
        return f"ID: {self.id_archivo} - Nombre: {self.name_archivo} - Tipo: {self.tipo_archivo.tipo_archivo} -Post: {self.post.descripcion_post}"
    
class Direccion(models.Model):
    pais = models. CharField(max_length=60)
    ciudad= models.CharField(max_length=60)
    localidad= models.CharField(max_length=60)

    def __str__(self):
        return f"{self.localidad}, {self.ciudad}, {self.pais}"


    @classmethod
    def registrar_direccion(cls, pais, ciudad, localidad):
        nueva_direccion = cls(pais=pais, ciudad=ciudad, localidad=localidad)
        nueva_direccion.save()
        return nueva_direccion
    
    @classmethod
    def buscar_direccion(cls, pais, ciudad, localidad):
        # Convertir los parámetros a minúsculas
        pais = pais.lower()
        ciudad = ciudad.lower()
        localidad = localidad.lower()

        # Realizar la búsqueda insensible a mayúsculas y minúsculas
        try:
            direccion = cls.objects.get(pais__icontains=pais, ciudad__icontains=ciudad, localidad__icontains=localidad)
            return direccion
        except cls.DoesNotExist:
            return None

class Chat (models.Model):
    cita = models.ForeignKey('Salida', on_delete= models.CASCADE)
    fecha_chat= models.DateField(auto_now_add= True)
    activo_chat=models.BooleanField(default=True)

class Favorito(models.Model):
    id_cliente= models.ForeignKey("Cliente", on_delete= models.CASCADE)
    id_amigo = models.ForeignKey("Amigo", on_delete=models.CASCADE)
    fecha_agregado= models.DateField(auto_now_add=True)