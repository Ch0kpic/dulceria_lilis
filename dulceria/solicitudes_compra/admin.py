from django.contrib import admin
from django.utils.html import format_html
from .models import SolicitudCompra, DetalleSolicitudCompra

class DetalleSolicitudCompraInline(admin.TabularInline):
    model = DetalleSolicitudCompra
    extra = 1
    fields = ('producto', 'cantidad_solicitada', 'precio_estimado', 'subtotal_display', 'observaciones')
    readonly_fields = ('subtotal_display',)
    
    def subtotal_display(self, obj):
        if obj.cantidad_solicitada and obj.precio_estimado:
            return f"${obj.subtotal:.2f}"
        return "-"
    subtotal_display.short_description = "Subtotal"

@admin.register(SolicitudCompra)
class SolicitudCompraAdmin(admin.ModelAdmin):
    list_display = ['numero_solicitud', 'fecha_solicitud', 'usuario_solicitante', 
                   'proveedor', 'estado_display', 'prioridad_display', 'total_display']
    list_filter = ['estado', 'prioridad', 'fecha_solicitud', 'proveedor']
    search_fields = ['numero_solicitud', 'usuario_solicitante__nombre', 
                    'usuario_solicitante__apellido', 'proveedor__nombre']
    readonly_fields = ['numero_solicitud', 'fecha_solicitud', 'total_display', 'usuario_solicitante']
    inlines = [DetalleSolicitudCompraInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_solicitud', 'usuario_solicitante', 'fecha_solicitud')
        }),
        ('Detalles de la Solicitud', {
            'fields': ('proveedor', 'estado', 'prioridad', 'fecha_requerida')
        }),
        ('Aprobación', {
            'fields': ('usuario_aprobador', 'fecha_aprobacion'),
            'classes': ('collapse',)
        }),
        ('Observaciones', {
            'fields': ('observaciones',)
        }),
        ('Total', {
            'fields': ('total_display',)
        }),
    )
    
    def estado_display(self, obj):
        colors = {
            'pendiente': 'orange',
            'aprobada': 'green',
            'rechazada': 'red',
            'en_proceso': 'blue',
            'completada': 'purple'
        }
        color = colors.get(obj.estado, 'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_estado_display()
        )
    estado_display.short_description = "Estado"
    
    def prioridad_display(self, obj):
        colors = {
            'alta': 'red',
            'media': 'orange',
            'baja': 'green'
        }
        color = colors.get(obj.prioridad, 'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_prioridad_display()
        )
    prioridad_display.short_description = "Prioridad"
    
    def total_display(self, obj):
        return format_html(
            '<span style="color: green; font-weight: bold;">${:.2f}</span>',
            obj.total
        )
    total_display.short_description = "Total"
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuario_solicitante = request.user
        super().save_model(request, obj, form, change)

@admin.register(DetalleSolicitudCompra)
class DetalleSolicitudCompraAdmin(admin.ModelAdmin):
    list_display = ['solicitud', 'producto', 'cantidad_solicitada', 'precio_estimado', 'subtotal_display']
    list_filter = ['solicitud__estado', 'producto']
    search_fields = ['solicitud__numero_solicitud', 'producto__nombre']
    
    def subtotal_display(self, obj):
        return format_html(
            '<span style="color: green; font-weight: bold;">${:.2f}</span>',
            obj.subtotal
        )
    subtotal_display.short_description = "Subtotal"