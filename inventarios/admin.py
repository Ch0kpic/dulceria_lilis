from django.contrib import admin
from .models import Inventario

class InventarioInline(admin.TabularInline):
    model = Inventario
    extra = 1
    fields = ('id_producto', 'cantidad_actual', 'ubicacion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'id_producto', 'cantidad_actual', 'ubicacion', 'fecha_ultima_actualizacion')
    search_fields = ('id_producto__nombre', 'ubicacion')
    list_filter = ('ubicacion', 'fecha_ultima_actualizacion')
    ordering = ('-fecha_ultima_actualizacion',)
    list_select_related = ('id_producto',)
    
    def has_module_permission(self, request):
        """Controlar acceso al módulo de inventarios"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            # Solo administradores pueden ver inventarios
            return user_role == 'Administrador'
        return request.user.is_superuser
    
    fieldsets = (
        ('Información del Inventario', {
            'fields': ('id_producto', 'cantidad_actual', 'ubicacion')
        }),
        ('Control de Fechas', {
            'fields': ('fecha_ultima_actualizacion',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Filtrar datos según el rol del usuario"""
        qs = super().get_queryset(request)
        
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            
            if user_role == 'Vendedor':
                # Los vendedores solo pueden ver inventarios con stock > 0
                qs = qs.filter(cantidad_actual__gt=0)
            elif user_role == 'Bodeguero':
                # Los bodegueros pueden ver todos los inventarios
                pass
            elif user_role == 'Cliente':
                # Los clientes no deberían acceder aquí (bloqueado por middleware)
                qs = qs.none()
        
        return qs
    
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
            return user_role in ['Administrador', 'Bodeguero']
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        """Controlar permisos de eliminar según rol"""
        if hasattr(request.user, 'id_rol'):
            user_role = request.user.id_rol.nombre
            return user_role == 'Administrador'
        return request.user.is_superuser
    
    def actualizar_stock(self, request, queryset):
        """Acción personalizada para actualizar stock"""
        updated = queryset.update(cantidad_actual=100)  # Ejemplo: resetear a 100
        self.message_user(request, f'{updated} registros de inventario actualizados.')
    actualizar_stock.short_description = "Actualizar stock a 100 unidades"
    
    actions = ['actualizar_stock']
