from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField()
    genero = models.CharField(
        max_length=50,
        choices=[('Hombre','Hombre'),('Mujer','Mujer')]
    )
    def __str__(self):
        return self.user.username


class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField()
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return f'id: {self.id} titulo: {self.titulo}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    publicacion= models.ForeignKey('Publicacion', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class DesL(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.pregunta
    
class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class LikePublicacion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.publicacion)

class Pregunta(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
