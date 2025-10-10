from django.contrib import admin
from django.utils.html import format_html
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio_formateado', 'en_inventario')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('precio_referencia',)
    ordering = ('nombre',)
    
    def precio_formateado(self, obj):
        return format_html('<strong>${}</strong>', f'{obj.precio_referencia:,.2f}')
    precio_formateado.short_description = 'Precio'
    precio_formateado.admin_order_field = 'precio_referencia'
    
    def en_inventario(self, obj):
        # Verificar si existe en inventario
        inventarios = obj.inventario_set.all()
        if inventarios.exists():
            total_stock = sum(inv.cantidad_actual for inv in inventarios)
            if total_stock > 0:
                return format_html('<span style="color: green;">✓ Stock: {}</span>', str(total_stock))
            else:
                return format_html('<span style="color: red;">✗ Sin Stock</span>')
        return format_html('<span style="color: orange;">No en inventario</span>')
    en_inventario.short_description = 'Estado Inventario'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar productos según permisos del rol
        if not request.user.is_superuser:
            if hasattr(request.user, 'id_rol') and request.user.id_rol:
                if not request.user.id_rol.puede_ver_productos:
                    qs = qs.none()
        return qs
