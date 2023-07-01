from django.urls import path
from rest_blog.views import *

urlpatterns = [
    path('lista_publicaciones', lista_publicaciones, name='lista_publicaciones'),
    path('lista_comentarios', lista_comentarios, name='lista_comentarios')
]
