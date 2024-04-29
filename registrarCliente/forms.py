from django import forms
from alquilarAmigo.models import Cliente

GENERO_CHOICES = (
    (1, 'Femenino'),
    (2, 'Masculino'),
    (3, 'No binario/Otro'),
    (4, 'Prefiero no decir'),
)
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'apellido', 'telefono', 'fecha_nacimiento',
            'ubicacion', 'correo', 'contrasena',
            'genero', 'descripcion'
            #, 'aviso_legal_aceptado','terminos_condiciones_aceptados'
        ]
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
