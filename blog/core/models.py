# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DesL(models.Model):
    id_pc = models.CharField(primary_key=True, max_length=100)
    pregunta_id_pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='pregunta_id_pregunta')
    comentario_id_com = models.ForeignKey(Comentario, models.DO_NOTHING, db_column='comentario_id_com')

    class Meta:
        managed = False
        db_table = 'des_l'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Foto(models.Model):
    id_foto = models.BigIntegerField(primary_key=True)
    nom_foto = models.CharField(max_length=30)
    post_id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='post_id_post')

    class Meta:
        managed = False
        db_table = 'foto'


class LikePost(models.Model):
    id_lp = models.BigIntegerField(primary_key=True)
    post_id_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='post_id_post')
    like_id_like = models.ForeignKey('Likes', models.DO_NOTHING, db_column='like_id_like')

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
    comentario = models.CharField(max_length=500)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    categoria_id_catego = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_catego')
    imagen = models.BinaryField(blank=True, null=True)

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
