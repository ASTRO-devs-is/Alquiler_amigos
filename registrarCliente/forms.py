from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'apellido', 'telefono', 'fecha_nacimiento',
            'pais', 'ciudad', 'localidad', 'email', 'contrasena',
            'genero', 'descripcion', 'aviso_legal_aceptado',
            'terminos_condiciones_aceptados'
        ]
        widgets = {
            'contrasena': forms.PasswordInput(),
        }