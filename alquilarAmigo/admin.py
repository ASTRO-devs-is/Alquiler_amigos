from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Salida, Categoria, Cliente, Amigo, DisponibilidadDias, DisponibilidadHoras
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

admin.site.register(Salida, SalidaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(DisponibilidadDias, DisponibilidadDiasAdmin)
admin.site.register(DisponibilidadHoras, DisponibilidadHorasAdmin)