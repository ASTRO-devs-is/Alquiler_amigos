from django import forms
from .models import FotoPerfil

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = FotoPerfil
        fields = ['image']