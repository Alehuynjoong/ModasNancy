from django import forms
from .models import Citas
from .models import RegistroUsuario
from .models import Catalogo

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        exclude = ['id']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroUsuario
        exclude = ['id']

class RegistroCatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        exclude = ['id']
