from django import forms
from django.forms import ModelForm
from .models import Comentario, Publicacion
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.forms.widgets import ClearableFileInput
import re
    
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
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'correo@ejemplo.com', 'id':'floatingTextarea2'})
        }
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'Añade un comentario...'}),
        }
        
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'imagen', 'biografia', 'genero']
        widgets = {
            'imagen': ClearableFileInput(),
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        pattern = r'^[a-zA-Z0-9]+$'  # Expresión regular para permitir solo letras mayúsculas, minúsculas y números
        if not re.match(pattern, username):
            raise forms.ValidationError('El nombre de usuario solo puede contener letras y números. SIN ESPACIOS')
        return username