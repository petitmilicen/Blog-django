from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField()
    biografia = models.TextField()
    genero = models.CharField(
        max_length=50,
        choices=[('Hombre','Hombre'),('Mujer','Mujer')]
    )
    rol = models.CharField(
    max_length=50,
    choices=[('Admin','Admin'),('Lector','Lector')], default='Lector') 
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField()
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Usuario, related_name='blog_publicaciones')
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Id: {self.id} | Titulo: {self.titulo} | Autor: {self.autor}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(default=None)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    autor =  models.ForeignKey(Usuario, related_name='usuario', on_delete=models.CASCADE, default=None)
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios',  on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return self.texto