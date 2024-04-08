from django import forms
import datetime
from datetime import timedelta
from alquilarAmigo.models import Tarifa
from alquilarAmigo.models import Amigo

import re

tarifa = list(Tarifa.objects.all().values_list('tarifa', 'tarifa'))
#tarifa = [(1, 2)]
GENERO_CHOICES = (
    (1, 'Femenino'),
    (2, 'Masculino'),
    (3, 'No binario/Otro'),
    (4, 'Prefiero no decir'),
)
class formularioRegistrarAmigo(forms.Form):
    genero = forms.ChoiceField(choices=GENERO_CHOICES, label='Género', 
                            widget=forms.RadioSelect())
    
    tarifa = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=tarifa, label='Tarifa', required=False)
    descripcion = forms.CharField(required=False, label='Descríbete', max_length=500, 
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Da una breve descripción de tí mismo',
                                    'rows': 4,
                                    'style': 'resize: none;'
                                }))
    fecha = forms.DateField(label='Fecha de nacimiento', required=False,
                            widget=forms.DateInput(attrs={"type": "date",'class': 'form-control'
                            }))
    nombre = forms.CharField(required=False, label='Nombre', max_length=50,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nombre'
                            }))
    apellido = forms.CharField(required=False, label='Apellido', 
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Apellido'
                            }))
    ciudad = forms.CharField(required=False, label='Ciudad', 
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Ciudad'
                            }))
    pais = forms.CharField(required=False, label='Paìs',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Paìs'
                            }))
    telefono = forms.CharField(required=False, label='Teléfono',
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Teléfono'
                                }))
    email = forms.CharField(required=False, label='Email', widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Email'
                                }))
    localidad = forms.CharField(required=False, label='Localidad',
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Localidad'
                                }))
    
    politica = forms.BooleanField(required=False, label='Acepto la politica de privacidad', 
                                widget=forms.CheckboxInput(attrs={
                                'class': 'form-check-input'
                                }))
    
    terminos = forms.BooleanField(required=False, label='Acepto los terminos y condiciones',
                                widget=forms.CheckboxInput(attrs={
                                'class': 'form-check-input'
                                }))

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        hoy = datetime.date.today()
        hace_18_anos = hoy - timedelta(days=18*365.25)  # Resta 18 años a la fecha actual
        if fecha is None:
            raise forms.ValidationError('La fecha no puede estar vacia')
        if fecha > hoy:
            raise forms.ValidationError('La fecha no puede ser mayor a la fecha actual')
        if fecha > hace_18_anos:
            raise forms.ValidationError('Debes tener al menos 18 años de edad')
        return fecha
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == "":
            raise forms.ValidationError('El email no puede estar vacio')
        if '@' not in email:
            raise forms.ValidationError('El email debe contener tener un formato valido')
        # Verificar si el correo electrónico termina con "@gmail.com" o "@hotmail.com"
        if not email.endswith('@gmail.com') and not email.endswith('@hotmail.com'):
            raise forms.ValidationError('El email debe ser de dominio @gmail.com o @hotmail.com')
        if Amigo.correo_duplicado(email):
            raise forms.ValidationError('El correo electrónico ya está registrado')

        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        
        # Verificar si el teléfono tiene exactamente 8 dígitos
        if len(telefono) != 8:
            raise forms.ValidationError('El teléfono debe tener exactamente 8 dígitos')
        if not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe contener solo numeros')
        return telefono
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == "":
            raise forms.ValidationError('El nombre no puede estar vacio')
        if re.search(r'\d', nombre):
            raise forms.ValidationError('El nombre no puede contener valores numéricos')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if apellido == "":
            raise forms.ValidationError('El apellido no puede estar vacio')
        if re.search(r'\d', apellido):
            raise forms.ValidationError('El apellido no puede contener valores numéricos')
        return apellido
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if not descripcion.strip():
            raise forms.ValidationError('La descripción no puede estar vacía')
        if len(descripcion) < 50:
            raise forms.ValidationError('La descripciòn debe tener al menos 50 caracteres')
        if len(descripcion) > 500:
            raise forms.ValidationError('La descripciòn no puede tener mas de 500 caracteres')
        
        # Contar el número de caracteres especiales permitidos en la descripción
        caracteres_especiales_permitidos = {'.', '$', '*', '+', '/', '-', ',', ';', '?', '¡', '¿', '&', '%', '#', '"'
                                            ,'1','2','3','4','5','6','7','8','9'}
        num_caracteres_especiales = sum(1 for char in descripcion if char in caracteres_especiales_permitidos)
    
            # Verificar si el número de caracteres especiales supera el límite
        if num_caracteres_especiales > 20:
            raise forms.ValidationError('La descripción no puede tener más de 20 caracteres especiales')
        return descripcion

    def clean_genero(self):
        genero = self.cleaned_data.get('genero')
        if not genero:
            raise forms.ValidationError('Debe seleccionar un género')
        return genero
    
    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad']
        if ciudad == "":
            raise forms.ValidationError('Ciudad no puede estar vacia')
        if re.search(r'\d', ciudad):
            raise forms.ValidationError('Ciudad no puede contener valores numéricos')
        return ciudad
    
    def clean_localidad(self):
        localidad = self.cleaned_data['localidad']
        if localidad == "":
            raise forms.ValidationError('La localidad no puede estar vacia')
        # Verificar si la localidad contiene al menos un carácter que no sea un número
        if not re.search(r'[^\d]', localidad):
            raise forms.ValidationError('La localidad debe contener al menos un carácter que no sea un número')
        return localidad
    
    def clean_pais(self):
        pais = self.cleaned_data['pais']
        if pais == "":
            raise forms.ValidationError('Paìs no puede estar vacio')
        if re.search(r'\d', pais):
            raise forms.ValidationError('Paìs no puede contener valores numéricos')
        return pais
    
    def clean_politica(self):
        politica = self.cleaned_data['politica']
        if politica is False:
            raise forms.ValidationError('Debes aceptar la polìtica de privacidad')
        return politica
    
    def clean_terminos(self):
        terminos = self.cleaned_data['terminos']
        if terminos is False:
            raise forms.ValidationError('Debes aceptar los tèrminos y condiciones')
        return terminos
