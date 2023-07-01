from django.urls import path
from rest_blog.views import lista_publicaciones

urlpatterns = [
    path('lista_publicaciones', lista_publicaciones, name='lista_publicaciones')
]
