from django.db import models

from django.db import models

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto_post = models.CharField(max_length=2000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=100, default='Habilitado')
    comentario_post = models.CharField(max_length=500, default=None)
    usuario_id_usuario = models.IntegerField(default=1)
    categoria_id_catego = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id_catego = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_categoria

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.TextField()
    fecha_creacion_com = models.DateField()
    status = models.CharField(max_length=300)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_comentario

class DesL(models.Model):
    id_pc = models.AutoField(primary_key=True)
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.pregunta

class Foto(models.Model):
    id_foto = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.nombre

class Like(models.Model):
    id_like = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_like)

class LikePost(models.Model):
    id_like_post = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_like_post)

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
    nom_usua = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    respuesta_seguridad = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_usua
