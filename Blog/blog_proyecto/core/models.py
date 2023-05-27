from django.db import models

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    autor = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField()
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        return f'id: {self.id_publicacion} titulo: {self.titulo}'

class Categoria(models.Model):
    id_catego = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)
    publicacion= models.ForeignKey('Publicacion', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class DesL(models.Model):
    id_pc = models.AutoField(primary_key=True)
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.pregunta
    
class Like(models.Model):
    id_like = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_like)

class LikePublicacion(models.Model):
    id_like_publicacion = models.AutoField(primary_key=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_like_publicacion)

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    respuesta_seguridad = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre
