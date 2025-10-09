from django.contrib import admin
from django.utils.html import format_html
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'contacto', 'direccion_corta', 'total_ventas')
    search_fields = ('nombre', 'contacto', 'direccion')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    
    def direccion_corta(self, obj):
        if len(obj.direccion) > 30:
            return obj.direccion[:30] + '...'
        return obj.direccion
    direccion_corta.short_description = 'Dirección'
    
    def total_ventas(self, obj):
        ventas_count = obj.venta_set.count()
        if ventas_count > 0:
            return format_html('<span style="color: green;">{} ventas</span>', ventas_count)
        else:
            return format_html('<span style="color: gray;">Sin ventas</span>')
    total_ventas.short_description = 'Total Ventas'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filtrar clientes según permisos del rol
        if not request.user.is_superuser:
            if hasattr(request.user, 'id_rol') and request.user.id_rol:
                if not request.user.id_rol.puede_ver_clientes:
                    qs = qs.none()
        return qs
