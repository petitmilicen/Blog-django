from django.shortcuts import render, redirect
from .models import *
from .forms import *

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

    if request.method == 'POST':
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        
        formulario = PublicacionForm()
        print(formulario.errors)
        
    context = {'form': formulario}
    return render(request, 'core/nueva-publicacion.html', context)

def registrarse(request):
    return render(request, 'core/registrarse.html')

def logearse(request):
    return render(request, 'core/logearse.html')