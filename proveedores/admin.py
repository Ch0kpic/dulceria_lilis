from django.contrib import admin
from .models import Proveedor, ProductoProveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'contacto', 'direccion', 'id_usuario_registro')
    search_fields = ('nombre', 'contacto')
    list_filter = ('id_usuario_registro',)
    ordering = ('nombre',)

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_producto_proveedor', 'id_producto', 'id_proveedor', 'precio_acordado', 'fecha_registro')
    search_fields = ('id_producto__nombre', 'id_proveedor__nombre')
    list_filter = ('fecha_registro',)
    date_hierarchy = 'fecha_registro'
