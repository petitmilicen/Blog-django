# Generated by Django 4.2.1 on 2023-05-27 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_catego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id_like', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=15)),
                ('respuesta_seguridad', models.CharField(max_length=50)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.pregunta')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='')),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='LikePublicacion',
            fields=[
                ('id_like_publicacion', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.like')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.CreateModel(
            name='DesL',
            fields=[
                ('id_pc', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.comentario')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.publicacion'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
