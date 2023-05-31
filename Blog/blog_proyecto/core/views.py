from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import PublicacionForm, CrearUsuarioFormulario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    publicaciones = Publicacion.objects.order_by('-fecha_creacion')[:3]
    context = {'publicaciones':publicaciones}
    return render(request, 'core/index.html', context)

def publicaciones(request):
    return render(request, 'core/publicaciones.html')

def publicacion(request, pk):
    publicacion = Publicacion.objects.get(id=pk)
    
    context = {'publicacion':publicacion}
    return render(request, 'core/publicacion.html', context)

@user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('index'))
def panel_administracion(request):
    publicaciones = Publicacion.objects.all() 
    context = {'publicaciones':publicaciones}
    return render(request, 'core/panel-admin.html', context)

def donacion(request):
    return render(request, 'core/donacion.html')

@user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('index'))
def nueva_publicacion(request):
    formulario = PublicacionForm()

    if request.method == 'POST':
        formulario = PublicacionForm(request.POST, request.FILES)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = User.objects.get(username=request.user)

            formulario.save()
            return redirect('panel-admin')
        
    context = {'form': formulario}
    return render(request, 'core/nueva-publicacion.html', context)

@user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('index'))
def editar_publicacion(request, pk):
    publicacion = Publicacion.objects.get(id=pk)
    form = PublicacionForm(instance=publicacion)

    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('panel-admin')

    context = {'form': form}
    return render(request, 'core/editar-publicacion.html', context)

@user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('index'))
def eliminar_publicacion(request, pk):
    
    publicacion = Publicacion.objects.get(id=pk)
    if request.method == 'POST':
        
        publicacion.delete()
        return redirect('panel-admin')

    context = {'publicacion': publicacion}
    return render(request, 'core/eliminar-publicacion.html', context)

def registrarse(request):
    formulario = CrearUsuarioFormulario()
    
    if request.method == 'POST':
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, 'La cuenta fue creada para' + ' ' + usuario)
            return redirect('logearse')

    context = {'form':formulario}
    return render(request, 'core/registrarse.html', context)

def logearse(request):
    if request.method == 'POST':
        usuario = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')
        
        user = authenticate(request, username=usuario, password=contrasena)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Usuario o contraseña es incorrecto')

    return render(request, 'core/logearse.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('logearse')

