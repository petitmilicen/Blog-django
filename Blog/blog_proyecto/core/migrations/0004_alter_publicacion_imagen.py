# Generated by Django 4.2.1 on 2023-07-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
