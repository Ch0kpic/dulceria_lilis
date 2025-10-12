from django.contrib import admin
from django.db.models import Q
from .models import Producto
from inventarios.admin import InventarioInline

class PrecioFilter(admin.SimpleListFilter):
    title = 'Rango de Precio'
    parameter_name = 'precio_rango'

    def lookups(self, request, model_admin):
        return (
            ('0-10000', 'Hasta $10,000'),
            ('10000-50000', '$10,000 - $50,000'),
            ('50000-100000', '$50,000 - $100,000'),
            ('100000+', 'Más de $100,000'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-10000':
            return queryset.filter(precio_referencia__lte=10000)
        elif self.value() == '10000-50000':
            return queryset.filter(precio_referencia__gte=10000, precio_referencia__lte=50000)
        elif self.value() == '50000-100000':
            return queryset.filter(precio_referencia__gte=50000, precio_referencia__lte=100000)
        elif self.value() == '100000+':
            return queryset.filter(precio_referencia__gte=100000)
        return queryset

class LetraInicialFilter(admin.SimpleListFilter):
    title = 'Letra Inicial'
    parameter_name = 'letra_inicial'

    def lookups(self, request, model_admin):
        # Obtener las primeras letras de los nombres de productos
        letras = Producto.objects.values_list('nombre', flat=True)
        letras_unicas = sorted(set([nombre[0].upper() for nombre in letras if nombre]))
        return [(letra, letra) for letra in letras_unicas]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(nombre__istartswith=self.value())
        return queryset

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio_referencia')
    search_fields = ('nombre', 'descripcion')
    list_filter = (PrecioFilter, LetraInicialFilter)
    ordering = ('nombre',)
    list_select_related = ()
    
    def has_module_permission(self, request):
        """Controlar acceso al módulo de productos"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            # Administradores y Bodegueros pueden ver productos
            return user_role in ['Administrador', 'Bodeguero']
        return request.user.is_superuser
    
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion', 'precio_referencia')
        }),
    )
    
    inlines = [InventarioInline]
    
    def has_add_permission(self, request):
        """Controlar permisos de agregar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role in ['Administrador', 'Bodeguero']
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        """Controlar permisos de editar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            # Solo administradores pueden modificar productos existentes
            return user_role == 'Administrador'
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        """Controlar permisos de eliminar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role == 'Administrador'
        return request.user.is_superuser
