from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'imagen', 'biografia', 'genero', 'rol', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('email', 'imagen', 'biografia', 'genero', 'rol')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Usuario, UsuarioAdmin)