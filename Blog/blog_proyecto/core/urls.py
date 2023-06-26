from django.urls import path
from core.views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/<str:pk>/', views.perfil, name='perfil'),
    path('editar-perfil/<int:pk>/', PerfilUpdateView.as_view(), name='editar-perfil'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('publicacion/<str:pk>/', views.publicacion, name='publicacion'),
    path('donacion/', views.donacion, name='donacion'),
    path('logearse/', views.logearse, name='logearse'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar-sesion'),
    path('nueva-publicacion/', views.nueva_publicacion, name='nueva-publicacion'),
    path('editar-publicacion/<str:pk>/', views.editar_publicacion, name='editar-publicacion'),
    path('eliminar-publicacion/<str:pk>/', views.eliminar_publicacion, name='eliminar-publicacion'),
    path('like-index/<str:pk>/', views.likes_index, name='like-index'),
    path('like-publicacion/<str:pk>/', views.likes_publicacion, name='like-publicacion'),
    path('like-publicaciones/<str:pk>/', views.likes_publicaciones, name='like-publicaciones'),
    path('panel-admin/', views.panel_administracion, name='panel-admin'),
    
    path('editar-comentario/<str:pk>/', views.editar_comentario, name='editar-comentario'),
    path('eliminar-comentario/<str:pk>/', views.eliminar_comentario, name='eliminar-comentario')
]
