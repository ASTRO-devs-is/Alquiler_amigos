import datetime
from datetime import datetime as dt, timedelta
from django import forms
from .models import Categoria



#categorias = list(Categoria.objects.all().values_list('nombre', 'nombre'))
categorias = [('cass', 'cass')]
class formularioProgramarCita(forms.Form):
    
    categorias = forms.ChoiceField(choices=categorias, label='Escoge la categoría de tu Salida', required=False,
    widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label='Escribe la descripción de tu salida',
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        'class': 'form-control', 
                                        'placeholder': 'Escribe aquí la descripción de tu salida',
                                        'style': 'resize: none;',
                                        'rows': 4
                                    })
                                )
    fecha = forms.DateField(label='Escoge la fecha de tu salida', required=False,
                            widget=forms.DateInput( attrs={"type": "date",'class': 'form-control'}))
    
    def clean_descripcion(self):
        ascii = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', 'ñ', 'Ñ', 'ü', 'Ü']
        ascii_rango = range(32,126)
        caracteresEspeciales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}',
                                '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '¡', '¿']
        descripcion = self.cleaned_data['descripcion']
        if descripcion == None or descripcion == '': 
            raise forms.ValidationError('La descripción no puede estar vacia')
        if len(descripcion) < 50:
            raise forms.ValidationError('La descripción debe tener al menos 50 caracteres')
        if len(descripcion) > 500:
            raise forms.ValidationError('La descripción no puede tener mas de 500 caracteres')
        contador = 0
        for caracter in descripcion:
            if caracter in caracteresEspeciales:
                contador += 1
        if contador > 20:
            raise forms.ValidationError('La descripción contiene mas de 20 caracteres especiales')
        for caracter in descripcion:
            if ord(caracter) not in ascii_rango and caracter not in ascii:
                raise forms.ValidationError('La descripción contiene caracteres no permitidos')
        return descripcion
        

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha == None:
            raise forms.ValidationError('La fecha no puede estar vacia')
        if fecha < datetime.date.today():
            raise forms.ValidationError('La fecha no puede ser menor a la fecha actual')
        if fecha > datetime.date.today() + datetime.timedelta(weeks=20):
            raise forms.ValidationError('La fecha no puede ser mayor a 4 meses de la fecha actual')
        return fecha

