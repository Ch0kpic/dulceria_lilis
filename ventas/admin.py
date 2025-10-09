from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum, F
from dulceria.admin_mixins import RoleBasedAdminMixin
from .models import Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    fields = ('id_producto', 'cantidad', 'precio_unitario', 'subtotal')
    readonly_fields = ('subtotal',)
    
    def subtotal(self, obj):
        if obj.cantidad and obj.precio_unitario:
            return format_html('<strong>${:,.2f}</strong>', obj.cantidad * obj.precio_unitario)
        return '$0.00'
    subtotal.short_description = 'Subtotal'

@admin.register(Venta)
class VentaAdmin(RoleBasedAdminMixin, admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_formateada', 'vendedor', 'cliente_nombre', 'total_venta', 'cantidad_items')
    search_fields = ('id_venta', 'id_usuario__nombre', 'id_cliente__nombre')
    list_filter = ('fecha', 'id_usuario', 'id_cliente')
    list_select_related = ('id_usuario', 'id_cliente')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    inlines = [DetalleVentaInline]
    
    def fecha_formateada(self, obj):
        return obj.fecha.strftime('%d/%m/%Y %H:%M')
    fecha_formateada.short_description = 'Fecha'
    fecha_formateada.admin_order_field = 'fecha'
    
    def vendedor(self, obj):
        return obj.id_usuario.nombre if obj.id_usuario else '-'
    vendedor.short_description = 'Vendedor'
    vendedor.admin_order_field = 'id_usuario__nombre'
    
    def cliente_nombre(self, obj):
        return obj.id_cliente.nombre if obj.id_cliente else '-'
    cliente_nombre.short_description = 'Cliente'
    cliente_nombre.admin_order_field = 'id_cliente__nombre'
    
    def total_venta(self, obj):
        total = obj.detalleventa_set.aggregate(
            total=Sum(F('cantidad') * F('precio_unitario'))
        )['total']
        if total:
            return format_html('<strong style="color: green;">${:,.2f}</strong>', total)
        return '$0.00'
    total_venta.short_description = 'Total'
    
    def cantidad_items(self, obj):
        count = obj.detalleventa_set.count()
        return format_html('<span style="color: blue;">{} items</span>', count)
    cantidad_items.short_description = 'Items'
    
    # Acción personalizada para marcar ventas como procesadas
    def marcar_procesadas(self, request, queryset):
        count = queryset.count()
        # Aquí podrías agregar lógica adicional
        self.message_user(request, f'{count} ventas marcadas como procesadas.')
    marcar_procesadas.short_description = "Marcar ventas seleccionadas como procesadas"
    
    actions = [marcar_procesadas]
    


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'venta_id', 'producto_nombre', 'cantidad', 'precio_formateado', 'subtotal_calculado')
    search_fields = ('id_venta__id_venta', 'id_producto__nombre')
    list_filter = ('id_venta__fecha', 'id_producto')
    list_select_related = ('id_venta', 'id_producto')
    ordering = ('-id_venta__fecha',)
    
    def venta_id(self, obj):
        return f"Venta #{obj.id_venta.id_venta}"
    venta_id.short_description = 'Venta'
    venta_id.admin_order_field = 'id_venta__id_venta'
    
    def producto_nombre(self, obj):
        return obj.id_producto.nombre
    producto_nombre.short_description = 'Producto'
    producto_nombre.admin_order_field = 'id_producto__nombre'
    
    def precio_formateado(self, obj):
        return format_html('${:,.2f}', obj.precio_unitario)
    precio_formateado.short_description = 'Precio Unit.'
    precio_formateado.admin_order_field = 'precio_unitario'
    
    def subtotal_calculado(self, obj):
        subtotal = obj.cantidad * obj.precio_unitario
        return format_html('<strong>${:,.2f}</strong>', subtotal)
    subtotal_calculado.short_description = 'Subtotal'
