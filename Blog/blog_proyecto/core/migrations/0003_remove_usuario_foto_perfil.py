# Generated by Django 4.2.1 on 2023-06-26 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto_perfil',
        ),
    ]
