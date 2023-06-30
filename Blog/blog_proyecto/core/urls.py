from django.urls import path
from core.views import *
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, SetPasswordFormForm

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
    path('eliminar-comentario/<str:pk>/', views.eliminar_comentario, name='eliminar-comentario'),
    
    #Recuperar contrasena, solo sirve localmente
    path('recuperar-contrasena/',
        auth_views.PasswordResetView.as_view(
        template_name='core/recuperar-contrasena.html',
        form_class=UserPasswordResetForm),
        name="recuperar-contrasena"),
    
    path('recuperar-contrasena-enviado/',
        auth_views.PasswordResetDoneView.as_view(
        template_name='core/recuperar-contrasena-enviado.html'),
        name='password_reset_done'),
    
    path('recuperar/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
        template_name='core/recuperar-contrasena-formulario.html',
        form_class=SetPasswordFormForm),
        name="password_reset_confirm"),
    
    path('recuperar-contrasena-completo/',
        auth_views.PasswordResetCompleteView.as_view(
        template_name='core/logearse.html'),
        name='password_reset_complete')
    
]
