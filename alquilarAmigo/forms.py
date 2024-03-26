from django import forms

categorias = [('Casual', 'Casual'), ('Deporte', 'Deporte'), ('Cultura', 'Cultura'), ('Cosplay', 'Cosplay'), ('Formal', 'Formal'), ('Virtual', 'Virtual')]

class formularioProgramarCita(forms.Form):
    categorias = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=categorias, label='Escoge la categoria de tu Salida', required=True)
    cajaTexto = forms.CharField(required=True, label='Escribe la descripcion de tu salida', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))