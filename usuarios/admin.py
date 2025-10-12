from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import Usuario

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'correo', 'nombre')

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('id_usuario', 'nombre', 'correo', 'id_rol', 'is_active', 'is_staff')
    search_fields = ('nombre', 'correo', 'username')
    list_filter = ('id_rol', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('nombre',)
    list_select_related = ('id_rol',)
    
    # Usar los formularios personalizados
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    def has_module_permission(self, request):
        """Controlar acceso al módulo de usuarios"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            # Solo administradores pueden ver usuarios
            return user_role == 'Administrador'
        return request.user.is_superuser
    
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
