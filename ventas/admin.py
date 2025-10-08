from django.contrib import admin
from .models import Venta, DetalleVenta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha', 'id_usuario', 'id_cliente')
    search_fields = ('id_venta', 'id_usuario__nombre', 'id_cliente__nombre')
    list_filter = ('fecha', 'id_usuario')
    date_hierarchy = 'fecha'

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'id_venta', 'id_producto', 'cantidad', 'precio_unitario')
    search_fields = ('id_venta__id_venta', 'id_producto__nombre')
    list_filter = ('id_venta__fecha',)
