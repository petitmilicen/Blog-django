from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def posts(request):
    return render(request, 'publicaciones.html')

def donacion(request):
    return render(request, 'donacion.html')

def nueva_publicacion(request):
    return render(request, 'nueva-publicacion.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def logearse(request):
    return render(request, 'logearse.html')