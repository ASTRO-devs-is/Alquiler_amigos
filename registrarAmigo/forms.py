from django import forms

tarifa = [('15 bs/hora', '15bs/hora'), ('25 bs/hora', '25 bs/hora'), ('50 bs/hora', '50 bs/hora'), ('75 bs/hora', '75 bs/hora'), ('100 bs/hora', '100 bs/hora')]

class formularioRegistrarAmigo(forms.Form):
    tarifa = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), 
                                    choices=tarifa, label='Tarifa', required=True)
    descripcion = forms.CharField(required=True, label='Describete', max_length=500, 
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Da una breve descripcion de ti mismo',
                                    'rows': 4,
                                    'auto-size': False
                                }))
    fecha = forms.DateField(label='Fecha de nacimiento', required=True,
                            widget=forms.DateInput(attrs={"type": "date",'class': 'form-control'
                            }))
    nombre = forms.CharField(required=True, label='Nombre', max_length=50,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nombre'
                            }))
    apellido = forms.CharField(required=True, label='Apellido', 
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nombre del amigo'
                            }))
    ciudad = forms.CharField(required=True, label='Ciudad', 
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Nombre del amigo'
                            }))
    pais = forms.CharField(required=True, label='Pais',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Pais'
                            }))
    telefono = forms.CharField(required=True, label='Telefono',
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Telefono'
                                }))
    email = forms.CharField(required=True, label='Email', widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Email'
                                }))
    localidad = forms.CharField(required=True, label='Localidad',
                                widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Localidad'
                                }))

    