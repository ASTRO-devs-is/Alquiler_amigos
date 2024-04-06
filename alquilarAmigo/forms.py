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
                                        'style': 'resize: none;',
                                        'rows': 4
                                    })
                                )
    fecha = forms.DateField(label='Escoge la fecha de tu salida', required=False,
                            widget=forms.DateInput( attrs={"type": "date",'class': 'form-control'}))
    
    def clean_cajaTexto(self):
        ascii = [164,165,168,173,160,130,161,162,163,181,144,214,224,233]
        ascii_rango = range(32,126)
        caracteresEspeciales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}',
                                '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '¡', '¿']
        cajaTexto = self.cleaned_data['cajaTexto']
        if cajaTexto == None or cajaTexto == '': 
            raise forms.ValidationError('La descripción no puede estar vacia')
        if len(cajaTexto) < 50:
            raise forms.ValidationError('La descripción debe tener al menos 50 caracteres')
        if len(cajaTexto) > 500:
            raise forms.ValidationError('La descripción no puede tener mas de 500 caracteres')
        contador = 0
        for caracter in cajaTexto:
            if caracter in caracteresEspeciales:
                contador += 1
        if contador > 20:
            raise forms.ValidationError('La descripción contiene mas de 20 caracteres especiales')
        for caracter in cajaTexto:
            if ord(caracter) not in ascii_rango and ord(caracter) not in ascii:
                raise forms.ValidationError('La descripción contiene caracteres no permitidos')
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
    def __init__(self, *args, **kwargs):
        self.horaInicioAux = None
        self.fecha_dada = None
        super(FormularioHoras, self).__init__( *args, **kwargs)
    

    horaInicio = forms.TimeField(label='Escoge la hora de inicio',required=False,
                                widget=forms.TimeInput( attrs={"type": "time",'class': 'form-control'}))
    horaFin = forms.TimeField(label='Escoge la hora de fin',required=False,
                            widget=forms.TimeInput(attrs={"type": "time",'class': 'form-control'}))
    
    def clean_horaInicio(self):
        
        horaInicio = self.cleaned_data['horaInicio']
        self.horaInicioAux = horaInicio
        if horaInicio is None:
            raise forms.ValidationError('La hora de inicio no puede estar vacia')

        if self.fecha_dada == datetime.date.today():
            if horaInicio < datetime.datetime.now().time():
                raise forms.ValidationError('La hora de inicio no puede ser menor a la hora actual')
            
        return horaInicio

    def clean_horaFin(self):
        horaFin = self.cleaned_data['horaFin']
        horaInicio = self.horaInicioAux
        if horaFin == None:
            raise forms.ValidationError('La hora de fin no puede estar vacia')
        if horaInicio is None:
            raise forms.ValidationError('Debe escoger una hora de inicio antes de escoger una hora de fin')
        
        if self.fecha_dada == datetime.date.today():
            if horaFin < datetime.datetime.now().time():
                raise forms.ValidationError('La hora de fin no puede ser menor a la hora actual')
        # Convertir a datetime
        ahora = dt.now()
        dt_horaInicio = dt.combine(ahora, horaInicio)
        dt_horaFin = dt.combine(ahora, horaFin)
        if dt_horaFin < dt_horaInicio:
            raise forms.ValidationError('La hora de fin no puede ser menor a la hora de inicio')
        if dt_horaFin - dt_horaInicio < timedelta(hours=1):
            raise forms.ValidationError('La duración de la salida debe ser de al menos 1 hora')
        if dt_horaFin - dt_horaInicio > timedelta(hours=2):
            raise forms.ValidationError('La duración de la salida no puede ser mayor a 2 horas')
        diferencia = dt_horaFin - dt_horaInicio
        minutos_diferencia = diferencia.seconds // 60
        if minutos_diferencia % 60 != 0:
            raise forms.ValidationError('La hora de fin debe ir de hora en hora') 
        return horaFin
