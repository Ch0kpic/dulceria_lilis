from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'username', 'nombre', 'correo', 'id_rol', 'is_active')
    search_fields = ('username', 'nombre', 'correo')
    list_filter = ('id_rol', 'is_active', 'is_staff')
    ordering = ('nombre',)
