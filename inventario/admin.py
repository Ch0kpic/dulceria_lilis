from django.contrib import admin
from .models import Inventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'id_producto', 'cantidad_actual', 'ubicacion', 'fecha_ultima_actualizacion')
    search_fields = ('id_producto__nombre', 'ubicacion')
    list_filter = ('fecha_ultima_actualizacion',)
    date_hierarchy = 'fecha_ultima_actualizacion'
