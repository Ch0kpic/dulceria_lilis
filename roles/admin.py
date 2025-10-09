from django.contrib import admin
from .models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre', 'tipo', 'descripcion', 'mostrar_permisos')
    search_fields = ('nombre', 'descripcion', 'tipo')
    list_filter = ('tipo', 'puede_ver_ventas', 'puede_crear_ventas', 'puede_ver_inventario')
    ordering = ('nombre',)
    
    fieldsets = (
        (None, {
            'fields': ('nombre', 'tipo', 'descripcion')
        }),
        ('Permisos de Ventas', {
            'fields': ('puede_ver_ventas', 'puede_crear_ventas')
        }),
        ('Permisos de Inventario', {
            'fields': ('puede_ver_inventario', 'puede_modificar_inventario')
        }),
        ('Permisos de Clientes', {
            'fields': ('puede_ver_clientes', 'puede_crear_clientes')
        }),
        ('Permisos de Proveedores', {
            'fields': ('puede_ver_proveedores', 'puede_crear_proveedores')
        }),
        ('Permisos de Productos', {
            'fields': ('puede_ver_productos', 'puede_crear_productos')
        }),
        ('Permisos de Usuarios', {
            'fields': ('puede_ver_usuarios', 'puede_crear_usuarios')
        }),
    )
    
    def mostrar_permisos(self, obj):
        permisos = []
        if obj.puede_ver_ventas: permisos.append('Ventas')
        if obj.puede_ver_inventario: permisos.append('Inventario')
        if obj.puede_ver_clientes: permisos.append('Clientes')
        if obj.puede_ver_proveedores: permisos.append('Proveedores')
        if obj.puede_ver_productos: permisos.append('Productos')
        if obj.puede_ver_usuarios: permisos.append('Usuarios')
        return ', '.join(permisos) if permisos else 'Sin permisos'
    mostrar_permisos.short_description = 'Módulos Permitidos'
