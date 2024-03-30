from django import forms
from .models import Cargar_Imagenes_Perfil

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Cargar_Imagenes_Perfil
        fields = ('photo',)