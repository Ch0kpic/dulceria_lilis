from django.contrib import admin
from .models import Producto
from inventarios.admin import InventarioInline

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio_referencia')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion', 'precio_referencia')
        }),
    )
    
    inlines = [InventarioInline]
    
    def has_add_permission(self, request):
        """Controlar permisos de agregar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role in ['Administrador', 'Bodeguero']
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        """Controlar permisos de editar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role in ['Administrador', 'Bodeguero']
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        """Controlar permisos de eliminar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role == 'Administrador'
        return request.user.is_superuser
