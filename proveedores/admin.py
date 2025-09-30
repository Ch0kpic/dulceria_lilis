from django.contrib import admin
from .models import Proveedor, ProductoProveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'contacto', 'telefono', 'direccion')
	search_fields = ('nombre', 'contacto', 'telefono')
	ordering = ('nombre',)

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
	list_display = ('producto', 'proveedor', 'precio', 'fecha_registro')
	search_fields = ('producto__nombre', 'proveedor__nombre')
	list_filter = ('proveedor',)
	ordering = ('producto', 'proveedor')
	list_select_related = ('producto', 'proveedor')
