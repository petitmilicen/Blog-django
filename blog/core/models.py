from django.db import models

from django.db import models

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto_post = models.CharField(max_length=2000)
    f_crea = models.DateField()
    estatus_post = models.CharField(max_length=100)
    comentario = models.CharField(max_length=500)
    usuario_id_usuario = models.IntegerField()
    categoria_id_catego = models.IntegerField()

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id_catego = models.IntegerField(primary_key=True)
    nom_catego = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    id_com = models.IntegerField(primary_key=True)
    texto_com = models.CharField(max_length=500)
    f_com = models.DateField()
    status_com = models.CharField(max_length=300)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')  # Cambio aquí
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class DesL(models.Model):
    id_pc = models.CharField(primary_key=True, max_length=100)
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_pc

class Foto(models.Model):
    id_foto = models.IntegerField(primary_key=True)
    nom_foto = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_foto

class Like(models.Model):
    id_like = models.IntegerField(primary_key=True)
    id_usua = models.IntegerField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_like)

class LikePost(models.Model):
    id_lp = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_lp)

class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    nom_pregu = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom_pregu

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nom_rol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nom_rol

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nom_usua = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    rut = models.IntegerField()
    f_nacim = models.DateField()
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    res_segu = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_usua
