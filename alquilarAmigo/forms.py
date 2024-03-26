from django import forms

categorias = [('Casual', 'Casual'), ('Deporte', 'Deporte'), ('Cultura', 'Cultura'), ('Cosplay', 'Cosplay'), ('Formal', 'Formal'), ('Virtual', 'Virtual')]

class formularioProgramarCita(forms.Form):
    categorias = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=categorias, label='Escoge la categoria de tu Salida', required=True)
    cajaTexto = forms.CharField(required=True, label='Escribe la descripcion de tu salida', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Escoge la fecha de tu salida', required=True,
                            widget=forms.DateInput(format="%d-%m-%Y", attrs={"type": "date",'class': 'form-control'}),
                            input_formats=["%d-%m-%Y"])
    horaInicio = forms.TimeField(label='Escoge la hora de Inicio', required=True, 
                            widget=forms.TimeInput(format="%H-%M", attrs={"type": "time",'class': 'form-control'}),
                            input_formats=["%H-%M"])
    horaFin = forms.TimeField(label='Escoge la hora de fin', required=True, 
                            widget=forms.TimeInput(format="%H-%M", attrs={"type": "time",'class': 'form-control'}),
                            input_formats=["%H-%M"])