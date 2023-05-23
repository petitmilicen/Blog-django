from django.db import models

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto_post = models.CharField(max_length=2000)