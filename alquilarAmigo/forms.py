import datetime
from django import forms
from .models import Salida



categorias = [('Casual', 'Casual'), ('Deporte', 'Deporte'), ('Cultura', 'Cultura'), ('Cosplay', 'Cosplay'), ('Formal', 'Formal'), ('Virtual', 'Virtual')]

class formularioProgramarCita(forms.Form):
    categorias = forms.ChoiceField(choices=categorias, label='Escoge la categoria de tu Salida', required=False,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    cajaTexto = forms.CharField(label='Escribe la descripcion de tu salida',required=False,
                                widget=forms.Textarea(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Escoge la fecha de tu salida', required=False,
                            widget=forms.DateInput( attrs={"type": "date",'class': 'form-control'}))
    horaInicio = forms.TimeField(label='Escoge la hora de Inicio',required=True,
                                widget=forms.TimeInput( attrs={"type": "time",'class': 'form-control'}))
    horaFin = forms.TimeField(label='Escoge la hora de fin',required=False,
                            widget=forms.TimeInput(attrs={"type": "time",'class': 'form-control'}))
    
    def clean_cajaTexto(self):
        cajaTexto = self.cleaned_data['cajaTexto']
        if cajaTexto == None or cajaTexto == '': 
            raise forms.ValidationError('La descripcion no puede estar vacia')
        return cajaTexto

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha == None:
            raise forms.ValidationError('La fecha no puede estar vacia')
        if fecha < datetime.date.today():
            raise forms.ValidationError('La fecha no puede ser menor a la fecha actual')
        if fecha > datetime.date.today() + datetime.timedelta(weeks=20):
            raise forms.ValidationError('La fecha no puede ser mayor a 20 semanas de la fecha actual')
        return fecha
    
    def clean_horaInicio(self):
        horaInicio = self.cleaned_data['horaInicio']
        if horaInicio == None:
            raise forms.ValidationError('La hora de inicio no puede estar vacia')
        if horaInicio < datetime.datetime.now().time():
            raise forms.ValidationError('La hora de inicio no puede ser menor a la hora actual')
        return horaInicio

    def clean_horaFin(self):
        horaFin = self.cleaned_data['horaFin']
        if horaFin == None:
            raise forms.ValidationError('La hora de fin no puede estar vacia')
        if horaFin < datetime.datetime.now().time():
            raise forms.ValidationError('La hora de fin no puede ser menor a la hora actual')
        return horaFin
    
    