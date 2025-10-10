from django.contrib import admin
from django import forms
from .models import Usuario
from roles.models import Rol

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'username', 'nombre', 'correo', 'id_rol', 'is_active', 'date_joined')
    search_fields = ('username', 'nombre', 'correo', 'id_rol__nombre')
    list_filter = ('id_rol', 'is_active', 'is_staff', 'date_joined')
    ordering = ('nombre',)
    list_select_related = ('id_rol',)
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('nombre', 'correo', 'first_name', 'last_name')
        }),
        ('Permisos', {
            'fields': ('id_rol', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filtrar roles según el usuario que está editando
        if db_field.name == "id_rol" and not request.user.is_superuser:
            # Excluir roles de administrador para usuarios no superuser
            kwargs["queryset"] = Rol.objects.exclude(
                nombre__icontains='Administrador'
            ).exclude(
                tipo='admin'
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Si no es superusuario, filtrar usuarios según el rol
        if not request.user.is_superuser:
            if hasattr(request.user, 'id_rol') and request.user.id_rol:
                if request.user.id_rol.tipo == 'jefe_ventas':
                    # Jefe de ventas solo ve vendedores y clientes
                    qs = qs.filter(id_rol__tipo__in=['vendedor', 'cliente'])
                elif request.user.id_rol.tipo == 'vendedor':
                    # Vendedores solo ven clientes
                    qs = qs.filter(id_rol__tipo='cliente')
                else:
                    # Otros roles no ven usuarios
                    qs = qs.none()
        return qs
