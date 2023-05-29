from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(DesL)
admin.site.register(Like)
admin.site.register(LikePublicacion)
admin.site.register(Pregunta)
admin.site.register(Usuario)

class AccountInLine(admin.StackedInline):
    model = Usuario
    can_delete = False
    
class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)