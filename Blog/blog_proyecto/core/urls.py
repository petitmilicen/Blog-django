from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('publicacion/<str:pk>/', views.publicacion, name='publicacion'),
    path('donacion/', views.donacion, name='donacion'),
    path('logearse/', views.logearse, name='logearse'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('nueva-publicacion/', views.nueva_publicacion, name='nueva-publicacion')

]