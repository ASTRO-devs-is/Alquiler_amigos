from django import forms

tarifa = [('15 bs/hora', '15bs/hora'), ('25 bs/hora', '25 bs/hora'), ('50 bs/hora', '50 bs/hora'), ('75 bs/hora', '75 bs/hora'), ('100 bs/hora', '100 bs/hora')]

class formularioRegistrarAmigo(forms.Form):
    tarifa = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=tarifa, label='', required=True)
    descripcion = forms.CharField(required=True, label='Escribe la tarifa', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Escoge la tarifa', required=True,
                            )
    nombre = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    apellido = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    ciudad = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    pais = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    telefono = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    email = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)
    localidad = forms.CharField(required=True, label='Escribe la descripcion', max_length=500)

    