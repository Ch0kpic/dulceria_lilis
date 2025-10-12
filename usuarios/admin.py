from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('id_usuario', 'nombre', 'correo', 'id_rol', 'is_active', 'is_staff')
    search_fields = ('nombre', 'correo', 'username')
    list_filter = ('id_rol', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('nombre',)
    list_select_related = ('id_rol',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'correo', 'contrasena')
        }),
        ('Rol y Permisos', {
            'fields': ('id_rol', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Datos de Autenticación', {
            'fields': ('username', 'password')
        }),
        ('Permisos', {
            'fields': ('groups', 'user_permissions')
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        ('Información Básica', {
            'classes': ('wide',),
            'fields': ('nombre', 'correo', 'username', 'password1', 'password2', 'id_rol'),
        }),
    )
