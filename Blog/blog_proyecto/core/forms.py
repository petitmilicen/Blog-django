from django import forms
from django.forms import ModelForm
from .models import Publicacion
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
    
class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'categoria','texto', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa un titulo'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ingresa el cuerpo de tu publicacion'})
        }

class CrearUsuarioFormulario(UserCreationForm):
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'**********'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'**********'})
    )
    
    class Meta:
        model = Usuario
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'correo@ejemplo.com'})
        }
        
    