from django.contrib import admin
from django.utils.html import format_html
from .models import Inventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'producto_nombre', 'estado_stock', 'ubicacion', 'alerta_stock', 'fecha_ultima_actualizacion')
    search_fields = ('id_producto__nombre', 'ubicacion')
    list_filter = ('fecha_ultima_actualizacion', 'ubicacion', 'cantidad_actual')
    list_select_related = ('id_producto',)
    date_hierarchy = 'fecha_ultima_actualizacion'
    ordering = ('-fecha_ultima_actualizacion',)
    
    fieldsets = (
        (None, {
            'fields': ('id_producto', 'ubicacion')
        }),
        ('Stock', {
            'fields': ('cantidad_actual', 'stock_minimo', 'stock_maximo')
        }),
    )
    
    def producto_nombre(self, obj):
        return obj.id_producto.nombre
    producto_nombre.short_description = 'Producto'
    producto_nombre.admin_order_field = 'id_producto__nombre'
    
    def estado_stock(self, obj):
        if obj.cantidad_actual > obj.stock_minimo:
            return format_html('<span style="color: green; font-weight: bold;">{} unidades</span>', obj.cantidad_actual)
        elif obj.cantidad_actual > 0:
            return format_html('<span style="color: red; font-weight: bold;">{} unidades (BAJO)</span>', obj.cantidad_actual)
        else:
            return format_html('<span style="color: red; font-weight: bold; background: yellow;">AGOTADO</span>')
    estado_stock.short_description = 'Stock'
    estado_stock.admin_order_field = 'cantidad_actual'
    
    def alerta_stock(self, obj):
        if obj.cantidad_actual <= obj.stock_minimo:
            return format_html('<span style="color: red; font-weight: bold;">⚠️ REPONER</span>')
        elif obj.cantidad_actual >= obj.stock_maximo:
            return format_html('<span style="color: blue; font-weight: bold;">📦 MÁXIMO</span>')
        else:
            return format_html('<span style="color: green;">✓ OK</span>')
    alerta_stock.short_description = 'Alerta'
    
    # Acción personalizada para reabastecer productos
    def reabastecer_stock(self, request, queryset):
        count = 0
        for inventario in queryset:
            if inventario.cantidad_actual < inventario.stock_minimo:
                # Reabastecer hasta el stock máximo
                cantidad_a_agregar = inventario.stock_maximo - inventario.cantidad_actual
                inventario.cantidad_actual = inventario.stock_maximo
                inventario.save()
                count += 1
        
        if count > 0:
            self.message_user(request, f'{count} productos reabastecidos exitosamente.')
        else:
            self.message_user(request, 'No hay productos que necesiten reabastecimiento.')
    reabastecer_stock.short_description = "Reabastecer productos con stock bajo"
    
    actions = [reabastecer_stock]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar inventario según permisos del rol
        if not request.user.is_superuser:
            if hasattr(request.user, 'id_rol') and request.user.id_rol:
                if not request.user.id_rol.puede_ver_inventario:
                    qs = qs.none()
        return qs
