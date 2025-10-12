from django.contrib import admin
from .models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    list_select_related = ()
    
    def has_module_permission(self, request):
        """Controlar acceso al módulo de roles"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            # Solo administradores pueden ver roles
            return user_role == 'Administrador'
        return request.user.is_superuser
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
    )
