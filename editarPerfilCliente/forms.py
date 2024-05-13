from django import forms
from alquilarAmigo.models import Cliente


class ClienteForm(forms.ModelForm):
    GENERO_CHOICES = [
        (1, 'Masculino'),
        (2, 'Femenino'),
        (3, 'No binario/otro'),
        (4, 'Prefiero no decir'),
    ]
    genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.RadioSelect)
    pais = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    localidad = forms.CharField(max_length=100)
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'apellido', 'telefono', 'fecha_nacimiento',
            'pais', 'ciudad', 'localidad', 'correo', 'contrasena',
            'genero', 'descripcion'
            #, 'aviso_legal_aceptado','terminos_condiciones_aceptados'
        ]
        widgets = {
            'contrasena': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
