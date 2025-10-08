from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio_referencia')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
