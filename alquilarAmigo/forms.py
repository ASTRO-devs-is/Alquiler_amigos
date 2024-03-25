from django import forms

categorias = [('Casual', 'Casual'), ('Deporte', 'Deporte'), ('Cultura', 'Cultura'), ('Cosplay', 'Cosplay'), ('Formal', 'Formal'), ('Virtual', 'Virtual')]

class formularioCategoria(forms.Form):
    categorias = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=categorias, label='Escoge la categoria de tu Salida', required=True)