from django.db import models

# Create your models here.

class User (models.Model):
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    activado = models.BooleanField(default = True)
    correo_electronico = models.EmailField(max_length=254)

    def __str__(self):
        return f"Nombre: {self.name_user} - Correo Electrónico: {self.correo_electronico} - Activo: {self.activado}"

    @classmethod
    def get_id_user(cls, nombre):
        try:
            user = cls.objects.get(name_user=nombre)
            return user.id_user
        except cls.DoesNotExist:
            return None

class Rol (models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=255)

    def __str__(self):
        return self.rol
    
class Funcion(models.Model):
    id_funcion = models. AutoField(primary_key=True)
    funcion = models.CharField(max_length=255)

    def __srt__(self):
        return self.funcion

class User_Rol(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    activo_ur = models.BooleanField(default=True)
    fecha_desde = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'rol')

class ROl_Funcion(models.Model):
    rol= models.ForeignKey(Rol, on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    activo_rf = models.BooleanField(default=True)

    class Meta:
        unique_together= ('rol', 'funcion')

class Categoria(models.Model):
    id_categoria= models.AutoField(primary_key=True)
    categoria = models.CharField(max_length= 255)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.categoria
    
class Interes(models.Model):
    id_interes = models.AutoField(primary_key= True)
    interes = models.CharField(max_length= 255)

    def __srt__(self):
        return self.interes
    
class User_Categoria (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    activo_uc = models.BooleanField(default=True)

    class Meta: 
        unique_together = ('user','categoria')

class Categoria_Interes(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)
    activo_ci= models.BooleanField(default= True)

    class Meta:
        unique_together= ('categoria', 'interes')

class Idioma (models.Model):
    id_idioma = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=255)

    def __srt__(self):
        return self.idioma
    
class User_Idioma(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    idioma =models.ForeignKey(Idioma, on_delete=models.CASCADE)
    activo_ui= models.BooleanField(default= True)

    class Meta:
        unique_together=('user', 'idioma')

class Reporte (models.Model):
    id_reporte= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reporte= models.CharField(max_length= 500)
    fecha_reporte= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reporte {self.id_reporte} - Usuario: {self.user.name_user}"
    
class Post (models.Model):
    id_post = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion_post =models.CharField(max_length=500)
    fecha_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reporte {self.id_post} - Usuario: {self.user.name_user}"
    
class Calificacion (models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    puntaje = models.IntegerField()
    fecha_calificacion= models.DateField(auto_now_add=True)
    
    
class Tipo_Archivo(models.Model):
    id_tipo_archivo = models.AutoField(primary_key=True)
    tipo_archivo = models.CharField(max_length = 50)

    def __srt__(self):
        return self.tipo_archivo
    
class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tipo_archivo = models.ForeignKey(Tipo_Archivo,on_delete=models.CASCADE)
    name_archivo = models.CharField(max_length = 255)
    archivo= models.BinaryField()
    fehca_archivo = models.DateField(auto_now_add=True)

    def __srt__(self):
        return f"ID: {self.id_archivo} - Nombre: {self.name_archivo} - Tipo: {self.tipo_archivo.tipo_archivo} -Post: {self.post.descripcion_post}"
    
#La clase Cliente se define como una subclase de User. 
#Cliente hereda todos los campos y métodos de User.
class Cliente(User):
    descripcion_cliente = models.CharField(max_length=700)

    def __str__(self):
        return f"Nombre: {self.name_user} - Acerca de mi: {self.descripcion_cliente}"
    
class Direccion(models.Model):
    id_direccion= models.AutoField(primary_key=True)
    pais = models. CharField()
    ciudad= models.CharField()
    localidad= models.CharField()

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

    


class Amigo (User):
    nombre_amigo= models.CharField(max_length = 255)
    apellidos_amigo = models.CharField(max_lenght= 500)
    fecha_nacimiento= models.DateField()
    numero_celular= models.IntegerField()
    ubicacion = models.ForeignKey(Direccion, on_delete=models.PROTECT)
    descripcion_amigo=models.CharField(max_lenght= 700)

    def __str__(self):
        return f"Nombre: {self.name_user} -Contacto: {self.numero_celular}- Acerca de mi: {self.descripcion_amigo}"

    @classmethod
    def registrar_amigo(cls, nombre, apellidos, fecha_nacimiento, numero_celular, ubicacion, descripcion):
        nuevo_amigo = cls(nombre_amigo=nombre, apellidos_amigo=apellidos, fecha_nacimiento=fecha_nacimiento, numero_celular=numero_celular, ubicacion=ubicacion, descripcion_amigo=descripcion)
        nuevo_amigo.save()
        return nuevo_amigo

class Tarifa (models.Model):
    id_tarifa = models.AutoField(primary_key=True)
    id_amigo= models.ForeignKey(User, on_delete= models.CASCADE)
    tarifa = models. IntegerField() 

    @classmethod
    def registrar_tarifa(cls, id_amigo, tarifa):
        nueva_tarifa = cls(id_amigo_id=id_amigo, tarifa=tarifa)
        nueva_tarifa.save()
        #return nueva_tarifa


class Horario (models.Model):
    id_horario = models.AutoField(primary_key=True)
    id_amigo = models.ForeignKey(User, on_delete=models.CASCADE)  
    fecha_hora_ini = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    horario_disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Amigo: {self.id_amigo} - Desde: {self.fecha_hora_ini} - Hasta: {self.fecha_hora_fin} - Disponible: {self.horario_disponible}"

class Cita (models.Model):
    id_cita= models.AutoField(primary_key=True)
    id_amigo = models.ForeignKey(User, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora_ini = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    cita_realizada = models.BooleanField(default=False)

class Chat (models.Model):
    id_chat = models.AutoField(primary_key=True)
    cita = models.ForeignKey(Cita, on_delete= models.CASCADE)
    fecha_chat= models.DateField(auto_now_add= True)
    activo_chat=models.BooleanField(default=True)

class Favorito(models.Model):
    id_favorito= models.AutoField(primary_key=True)
    id_cliente= models.ForeignKey(User, on_delete= models.CASCADE)
    id_amigo = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_agregado= models.DateField(auto_now_add=True)

 
        




