from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField()
    biografia = models.TextField(null=True)
    genero = models.CharField(
        max_length=50,
        choices=[('Hombre','Hombre'),('Mujer','Mujer')]
    )
    rol = models.CharField(
    max_length=50,
    choices=[('Admin','Admin'),('Lector','Lector')],
    default=None)
    def __str__(self):
        return self.user.username

class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField()
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_publicaciones')
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Id: {self.id} | Titulo: {self.titulo} | Autor: {self.autor}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(default=None)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    usuario =  models.ForeignKey(Usuario, related_name='usuario', on_delete=models.CASCADE, default=None)
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios',  on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return self.texto