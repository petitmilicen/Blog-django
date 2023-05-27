from django.shortcuts import render
from .models import *

def index(request):
    publicaciones = Publicacion.objects.all()
    
    context = {'publicaciones':publicaciones}
    return render(request, 'core/index.html', context)

def publicaciones(request):
    return render(request, 'core/publicaciones.html')

def publicacion(request, pk):
    publicacion = Publicacion.objects.get(id_publicacion=pk)
    
    context = {'publicacion':publicacion}
    return render(request, 'core/publicacion.html', context)

def donacion(request):
    return render(request, 'core/donacion.html')

def nueva_publicacion(request):
    return render(request, 'core/nueva-publicacion.html')

def registrarse(request):
    return render(request, 'core/registrarse.html')

def logearse(request):
    return render(request, 'core/logearse.html')