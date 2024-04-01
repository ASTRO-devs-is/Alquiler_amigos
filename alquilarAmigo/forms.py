import datetime
from datetime import datetime as dt, timedelta
from django import forms
from .models import Categoria



categorias = list(Categoria.objects.all().values_list('nombre', 'nombre'))
#categorias = [('cass', 'cass')]
class formularioProgramarCita(forms.Form):
    categorias = forms.ChoiceField(choices=categorias, label='Escoge la categoría de tu Salida', required=False,
    widget=forms.Select(attrs={'class': 'form-control'}))
    cajaTexto = forms.CharField(label='Escribe la descripción de tu salida',
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        'class': 'form-control', 
                                        'placeholder': 'Escribe aqui la descripción de tu salida',
                                        'style': 'resize: none;'
                                    })
                                )
    fecha = forms.DateField(label='Escoge la fecha de tu salida', required=False,
                            widget=forms.DateInput( attrs={"type": "date",'class': 'form-control'}))
    
    def clean_cajaTexto(self):
        cajaTexto = self.cleaned_data['cajaTexto']
        if cajaTexto == None or cajaTexto == '': 
            raise forms.ValidationError('La descripción no puede estar vacia')
        if len(cajaTexto) < 50:
            raise forms.ValidationError('La descripción debe tener al menos 50 caracteres')
        if len(cajaTexto) > 500:
            raise forms.ValidationError('La descripción no puede tener mas de 500 caracteres')
        return cajaTexto

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha == None:
            raise forms.ValidationError('La fecha no puede estar vacia')
        if fecha < datetime.date.today():
            raise forms.ValidationError('La fecha no puede ser menor a la fecha actual')
        if fecha > datetime.date.today() + datetime.timedelta(weeks=20):
            raise forms.ValidationError('La fecha no puede ser mayor a 4 meses de la fecha actual')
        return fecha

class FormularioHoras(forms.Form):
    horaInicio = forms.TimeField(label='Escoge la hora de inicio',required=False,
                                widget=forms.TimeInput( attrs={"type": "time",'class': 'form-control'}))
    horaFin = forms.TimeField(label='Escoge la hora de fin',required=False,
                            widget=forms.TimeInput(attrs={"type": "time",'class': 'form-control'}))
    
    def clean_horaInicio(self):
        horaInicio = self.cleaned_data['horaInicio']
        if horaInicio is None:
            raise forms.ValidationError('La hora de inicio no puede estar vacia')
        if horaInicio < datetime.datetime.now().time():
            raise forms.ValidationError('La hora de inicio no puede ser menor a la hora actual')

    def clean_horaFin(self):
        horaFin = self.cleaned_data['horaFin']
        horaInicio = self.cleaned_data.get('horaInicio')
        if horaFin == None:
            raise forms.ValidationError('La hora de fin no puede estar vacia')
        if horaFin < datetime.datetime.now().time():
            raise forms.ValidationError('La hora de fin no puede ser menor a la hora actual')
        # Convertir a datetime
        if horaInicio is not None:
            ahora = dt.now()
            dt_horaInicio = dt.combine(ahora, horaInicio)
            dt_horaFin = dt.combine(ahora, horaFin)

            if dt_horaFin - dt_horaInicio < timedelta(hours=1):
                raise forms.ValidationError('La duración de la salida debe ser de al menos 1 hora')
            diferencia = dt_horaFin - dt_horaInicio
            minutos_diferencia = diferencia.seconds // 60

            if minutos_diferencia % 30 != 0:
                raise forms.ValidationError('La hora de fin debe ser igual a la hora de inicio o aumentar en incrementos de 30 minutos')        
        return horaFin
