from django import forms
from django.forms import ModelForm
from .models import Comentario, Publicacion
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth import views
import re
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
    
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
        fields = ['username', 'email', 'imagen', 'biografia', 'genero']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        pattern = r'^[a-zA-Z0-9]+$'  # Expresión regular para permitir solo letras mayúsculas, minúsculas y números
        if not re.match(pattern, username):
            raise forms.ValidationError('El nombre de usuario solo puede contener letras y números. SIN ESPACIOS')
        return username
    
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingresa tu correo',
        'type': 'email',
        'name': 'email'
        }))
    
class SetPasswordFormForm(SetPasswordForm):

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'**********'}),

    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'**********'}),
    )