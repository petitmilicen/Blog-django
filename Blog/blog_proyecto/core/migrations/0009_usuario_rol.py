# Generated by Django 4.2.1 on 2023-06-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_comentario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Lector', 'Lector')], default=None, max_length=50),
        ),
    ]
