from django.contrib import admin
from django.core.exceptions import PermissionDenied

class RoleBasedAdminMixin:
    """
    Mixin para administrar permisos basados en roles en el admin de Django
    """
    
    def get_queryset(self, request):
        """Filtrar queryset basado en el rol del usuario"""
        qs = super().get_queryset(request)
        
        # Los superusuarios ven todo
        if request.user.is_superuser:
            return qs
            
        # Verificar si el usuario tiene rol asignado
        if not hasattr(request.user, 'id_rol') or not request.user.id_rol:
            return qs.none()
            
        rol = request.user.id_rol
        
        # Aplicar filtros según el tipo de modelo
        model_name = self.model._meta.model_name
        
        # Filtros específicos por modelo
        if model_name == 'venta':
            if not rol.puede_ver_ventas:
                return qs.none()
            # Los vendedores solo ven sus propias ventas
            if rol.tipo == 'vendedor':
                return qs.filter(id_usuario=request.user)
                
        elif model_name == 'inventario':
            if not rol.puede_ver_inventario:
                return qs.none()
                
        elif model_name == 'cliente':
            if not rol.puede_ver_clientes:
                return qs.none()
                
        elif model_name == 'proveedor':
            if not rol.puede_ver_proveedores:
                return qs.none()
            # Los bodegueros solo ven proveedores que ellos registraron
            if rol.tipo == 'bodeguero':
                return qs.filter(id_usuario_registro=request.user)
                
        elif model_name == 'producto':
            if not rol.puede_ver_productos:
                return qs.none()
                
        elif model_name == 'usuario':
            if not rol.puede_ver_usuarios:
                return qs.none()
            # Filtrar usuarios según jerarquía
            if rol.tipo == 'jefe_ventas':
                return qs.filter(id_rol__tipo__in=['vendedor', 'cliente'])
            elif rol.tipo == 'vendedor':
                return qs.filter(id_rol__tipo='cliente')
        
        return qs
    
    def has_add_permission(self, request):
        """Verificar permisos de creación"""
        if not super().has_add_permission(request):
            return False
            
        if request.user.is_superuser:
            return True
            
        if not hasattr(request.user, 'id_rol') or not request.user.id_rol:
            return False
            
        rol = request.user.id_rol
        model_name = self.model._meta.model_name
        
        permission_map = {
            'venta': rol.puede_crear_ventas,
            'cliente': rol.puede_crear_clientes,
            'proveedor': rol.puede_crear_proveedores,
            'producto': rol.puede_crear_productos,
            'usuario': rol.puede_crear_usuarios,
        }
        
        return permission_map.get(model_name, False)
    
    def has_change_permission(self, request, obj=None):
        """Verificar permisos de modificación"""
        if not super().has_change_permission(request, obj):
            return False
            
        if request.user.is_superuser:
            return True
            
        if not hasattr(request.user, 'id_rol') or not request.user.id_rol:
            return False
            
        rol = request.user.id_rol
        model_name = self.model._meta.model_name
        
        # Para inventario, verificar si puede modificar
        if model_name == 'inventario' and not rol.puede_modificar_inventario:
            return False
            
        # Los vendedores solo pueden modificar sus propias ventas
        if model_name == 'venta' and rol.tipo == 'vendedor':
            if obj and obj.id_usuario != request.user:
                return False
                
        return self.has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        """Verificar permisos de eliminación"""
        if not super().has_delete_permission(request, obj):
            return False
            
        # Solo administradores pueden eliminar
        if request.user.is_superuser:
            return True
            
        if hasattr(request.user, 'id_rol') and request.user.id_rol:
            return request.user.id_rol.tipo == 'admin'
            
        return False

class OrganizationFilterMixin:
    """
    Mixin para filtrar por organización (para proyectos como EcoEnergy)
    """
    organization_field = 'organizacion'  # Campo que relaciona con la organización
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
            
        # Filtrar por la organización del usuario
        if hasattr(request.user, self.organization_field):
            filter_kwargs = {
                self.organization_field: getattr(request.user, self.organization_field)
            }
            return qs.filter(**filter_kwargs)
            
        return qs.none()
    
    def save_model(self, request, obj, form, change):
        """Asignar automáticamente la organización del usuario al guardar"""
        if not change and hasattr(request.user, self.organization_field):
            setattr(obj, self.organization_field, getattr(request.user, self.organization_field))
        super().save_model(request, obj, form, change)