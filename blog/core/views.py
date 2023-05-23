from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def posts(request):
    return render(request, 'core/publicaciones.html')

def donacion(request):
    return render(request, 'core/donacion.html')

def nueva_publicacion(request):
    return render(request, 'core/nueva-publicacion.html')

def registrarse(request):
    return render(request, 'core/registrarse.html')

def logearse(request):
    return render(request, 'core/logearse.html')