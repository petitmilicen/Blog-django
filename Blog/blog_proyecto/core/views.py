from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import PublicacionForm, CrearUsuarioFormulario, ComentarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

def index(request):
    publicaciones = Publicacion.objects.order_by('-fecha_creacion')[:3]
    categorias = Categoria.objects.all()

    context = {'publicaciones':publicaciones, 'categorias':categorias}
    return render(request, 'core/index.html', context)

def publicaciones(request):
    pagina = Paginator(Publicacion.objects.all(), 3)
    pagina_numero = request.GET.get('pagina')
    pagina_objeto = pagina.get_page(pagina_numero)  
    
    request.session['pagina_numero'] = pagina_numero
    context = {'publicaciones':pagina_objeto}
    
    return render(request, 'core/publicaciones.html', context)

def publicacion(request, pk):
    publicacion = Publicacion.objects.get(id=pk)
    formulario_comentario = ComentarioForm()

    if request.method == 'POST':
        formulario_comentario = ComentarioForm(request.POST)
        if formulario_comentario.is_valid():
            comentario = formulario_comentario.save(commit=False)
            comentario.autor = Usuario.objects.get(username=request.user)
            comentario.publicacion = Publicacion.objects.get(id=pk)
            
            formulario_comentario.save()
            return HttpResponseRedirect(reverse('publicacion', args=[str(pk)]))

    context = {'publicacion':publicacion, 'formulario_comentario':formulario_comentario}
    return render(request, 'core/publicacion.html', context)

#Sistema de likes
@login_required
def likes_index(request, pk):
    publicacion = get_object_or_404(Publicacion, id=request.POST.get('publicacion-index-id'))
    
    if publicacion.likes.filter(id=request.user.id).exists():
        publicacion.likes.remove(request.user)
    else:
        publicacion.likes.add(request.user)
        
    return HttpResponseRedirect(reverse('index'))

@login_required
def likes_publicaciones(request, pk):
    publicacion = get_object_or_404(Publicacion, id=request.POST.get('publicaciones-id'))

    if publicacion.likes.filter(id = request.user.id).exists():
        publicacion.likes.remove(request.user)
    else:
        publicacion.likes.add(request.user)
        
    pagina_numero = request.session.get('pagina_numero', '')
    url_redireccion = reverse('publicaciones') + f'?pagina={pagina_numero}'

    return HttpResponseRedirect(url_redireccion)   

@login_required
def likes_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, id=request.POST.get('publicacion-id'))
    
    if publicacion.likes.filter(id = request.user.id).exists():
        publicacion.likes.remove(request.user)
    else:
        publicacion.likes.add(request.user)
        
    return HttpResponseRedirect(reverse('publicacion', args=[str(pk)]))

@user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('index'))
def panel_administracion(request):
    publicaciones = Publicacion.objects.all()
    comentarios = Comentario.objects.all()
    usuarios = Usuario.objects.all()
    
    
    context = {'publicaciones':publicaciones,'comentarios':comentarios,'usuarios':usuarios}
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
            publicacion.autor = Usuario.objects.get(username=request.user)

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

def perfil(request, pk):
    usuario = Usuario.objects.get(id=pk)
    comentarios = Comentario.objects.filter(autor=usuario)
    publicaciones = Publicacion.objects.filter(autor=usuario)
    
    context = {'usuario':usuario, 'publicaciones':publicaciones, 'comentarios':comentarios}
    return render(request, 'core/perfil.html', context)