from django.db import models

class Categoria(models.Model):
    id_catego = models.BigIntegerField(primary_key=True)
    nom_catego = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categoria'

class Comentario(models.Model):
    id_com = models.BigIntegerField(primary_key=True)
    texto_com = models.CharField(max_length=500)
    f_com = models.DateField()
    status_com = models.CharField(max_length=300)
    post_id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='post_id_post')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'comentario'

class LikePost(models.Model):
    id_lp = models.BigIntegerField(primary_key=True)
    post_id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='post_id_post')
    like_id_like = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'like_post'

class Likes(models.Model):
    id_like = models.BigIntegerField(primary_key=True)
    id_usua = models.BigIntegerField()
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'likes'

class Post(models.Model):
    id_post = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto_post = models.CharField(max_length=2000)
    f_crea = models.DateField()
    estatus_post = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=500)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    categoria_id_catego = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_catego')
    imagen = models.ImageField(upload_to=None, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'

class Pregunta(models.Model):
    id_pregunta = models.BigIntegerField(primary_key=True)
    nom_pregu = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pregunta'

class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nom_rol = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'rol'

class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nom_usua = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    rut = models.BigIntegerField()
    f_nacim = models.DateField()
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=20)
    nickname = models.CharField(max_length=15)
    res_segu = models.CharField(max_length=50)
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_id_rol')
    pregunta_id_pregunta = models.ForeignKey(Pregunta, models.DO_NOTHING, db_column='pregunta_id_pregunta')

    class Meta:
        managed = False
        db_table = 'usuario'
