from django.urls import path
from rest_blog.views import *

urlpatterns = [
    path('lista-publicaciones', lista_publicaciones, name='lista_publicaciones'),
    path('lista-comentarios', lista_comentarios, name='lista_comentarios'),
    
    path('detalle-publicacion/<id>', detalle_publicacion, name="detalle_publicacion"),
    path('detalle-comentario/<id>', detalle_comentario, name="detalle_comentario")
]
