from django import forms
import datetime
from datetime import timedelta
#from alquilarAmigo.models import Tarifa

#tarifa = [(tarifa.tarifa, str(tarifa.tarifa)) for tarifa in Tarifa.objects.all()]
tarifa = [(1, 2)]

class formularioRegistrarAmigo(forms.Form):
    tarifa = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=tarifa, label='Tarifa', required=False)
    descripcion = forms.CharField(required=False, label='Describete', max_length=500, 
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Da una breve descripcion de ti mismo',
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
    pais = forms.CharField(required=False, label='Pais',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Pais'
                            }))
    telefono = forms.CharField(required=False, label='Telefono',
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Telefono'
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
        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if len(telefono) > 8:
            raise forms.ValidationError('El telefono debe tener menos de 8 digitos')
        if not telefono.isdigit():
            raise forms.ValidationError('El telefono debe contener solo numeros')
        return telefono
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == "":
            raise forms.ValidationError('El nombre no puede estar vacio')
        return nombre
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if apellido == "":
            raise forms.ValidationError('El apellido no puede estar vacio')
        return apellido
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if descripcion == "":
            raise forms.ValidationError('La descripcion no puede estar vacia')
        if len(descripcion) < 10:
            raise forms.ValidationError('La descripcion debe tener al menos 10 caracteres')
        if len(descripcion) > 500:
            raise forms.ValidationError('La descripcion no puede tener mas de 500 caracteres')
        return descripcion
    
    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad']
        if ciudad == "":
            raise forms.ValidationError('La ciudad no puede estar vacia')
        return ciudad
    
    def clean_localidad(self):
        localidad = self.cleaned_data['localidad']
        if localidad == "":
            raise forms.ValidationError('La localidad no puede estar vacia')
        return localidad
    
    def clean_pais(self):
        pais = self.cleaned_data['pais']
        if pais == "":
            raise forms.ValidationError('El pais no puede estar vacio')
        return pais
    
    def clean_politica(self):
        politica = self.cleaned_data['politica']
        if politica is False:
            raise forms.ValidationError('Debes aceptar la politica de privacidad')
        return politica
    
    def clean_terminos(self):
        terminos = self.cleaned_data['terminos']
        if terminos is False:
            raise forms.ValidationError('Debes aceptar los terminos y condiciones')
        return terminos
