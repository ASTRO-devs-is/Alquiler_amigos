from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Salida, Categoria, Cliente, Amigo, DisponibilidadDias, DisponibilidadHoras, Tarifa, Direccion,User, Interes, User_Categoria, User_Interes
# Register your models here.

class SalidaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AmigoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class DisponibilidadDiasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class DisponibilidadHorasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class DireccionAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Salida, SalidaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(DisponibilidadDias, DisponibilidadDiasAdmin)
admin.site.register(DisponibilidadHoras, DisponibilidadHorasAdmin)
admin.site.register(Tarifa)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(User)
admin.site.register(Interes)
admin.site.register(User_Categoria)
admin.site.register(User_Interes)
