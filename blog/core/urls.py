from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicaciones/', views.posts, name='publicaciones'),
    path('donacion/', views.donacion, name='donacion')

]
