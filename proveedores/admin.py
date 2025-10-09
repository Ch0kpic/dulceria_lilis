from django.contrib import admin
from django.utils.html import format_html
from .models import Proveedor, ProductoProveedor

class ProductoProveedorInline(admin.TabularInline):
    model = ProductoProveedor
    extra = 1
    fields = ('id_producto', 'precio_acordado')
    
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'contacto', 'direccion_corta', 'usuario_registro', 'total_productos')
    search_fields = ('nombre', 'contacto', 'direccion', 'id_usuario_registro__nombre')
    list_filter = ('id_usuario_registro', 'fecha_registro')
    list_select_related = ('id_usuario_registro',)
    ordering = ('nombre',)
    inlines = [ProductoProveedorInline]
    
    def direccion_corta(self, obj):
        if len(obj.direccion) > 25:
            return obj.direccion[:25] + '...'
        return obj.direccion
    direccion_corta.short_description = 'Dirección'
    
    def usuario_registro(self, obj):
        return obj.id_usuario_registro.nombre if obj.id_usuario_registro else '-'
    usuario_registro.short_description = 'Registrado por'
    usuario_registro.admin_order_field = 'id_usuario_registro__nombre'
    
    def total_productos(self, obj):
        count = obj.productoproveedor_set.count()
        return format_html('<span style="color: blue; font-weight: bold;">{} productos</span>', count)
    total_productos.short_description = 'Productos'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar proveedores según permisos del rol
        if not request.user.is_superuser:
            if hasattr(request.user, 'id_rol') and request.user.id_rol:
                if not request.user.id_rol.puede_ver_proveedores:
                    qs = qs.none()
        return qs

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_producto_proveedor', 'producto_nombre', 'proveedor_nombre', 'precio_formateado', 'fecha_registro')
    search_fields = ('id_producto__nombre', 'id_proveedor__nombre')
    list_filter = ('fecha_registro', 'id_proveedor')
    list_select_related = ('id_producto', 'id_proveedor')
    date_hierarchy = 'fecha_registro'
    ordering = ('-fecha_registro',)
    
    def producto_nombre(self, obj):
        return obj.id_producto.nombre
    producto_nombre.short_description = 'Producto'
    producto_nombre.admin_order_field = 'id_producto__nombre'
    
    def proveedor_nombre(self, obj):
        return obj.id_proveedor.nombre
    proveedor_nombre.short_description = 'Proveedor'
    proveedor_nombre.admin_order_field = 'id_proveedor__nombre'
    
    def precio_formateado(self, obj):
        return format_html('<strong>${:,.2f}</strong>', obj.precio_acordado)
    precio_formateado.short_description = 'Precio'
    precio_formateado.admin_order_field = 'precio_acordado'
