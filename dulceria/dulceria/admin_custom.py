from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class RoleBasedAdminSite(AdminSite):
    """
    AdminSite personalizado que restringe el acceso según roles
    """
    site_header = "Dulcería Lilis - Administración"
    site_title = "Dulcería Lilis Admin"
    index_title = "Panel de Administración"
    
    def has_permission(self, request):
        """
        Verificar si el usuario tiene permisos para acceder al admin
        """
        if not request.user.is_active:
            return False
            
        if not hasattr(request.user, 'id_rol') or not request.user.id_rol:
            return False
            
        # Administradores, vendedores y bodegueros pueden acceder al admin
        allowed_roles = ['admin', 'vendedor', 'jefe_ventas', 'bodeguero']
        return request.user.id_rol.tipo in allowed_roles
    
    def index(self, request, extra_context=None):
        """
        Personalizar la página principal del admin según el rol
        """
        if not self.has_permission(request):
            return HttpResponseRedirect(reverse('login'))
            
        return super().index(request, extra_context)
    
    def _build_app_dict(self, request, label=None):
        """
        Filtrar las aplicaciones mostradas según el rol del usuario
        """
        app_dict = super()._build_app_dict(request, label)
        
        if not request.user.id_rol:
            return {}
            
        user_role = request.user.id_rol.tipo
        
        # Configurar qué módulos ve cada rol
        if user_role == 'admin':
            # El admin ve todo
            return app_dict
            
        elif user_role in ['vendedor', 'jefe_ventas']:
            # Vendedores solo ven módulos de ventas
            allowed_apps = ['productos', 'inventario', 'ventas', 'clientes']
            filtered_dict = {}
            
            for app_label, app_data in app_dict.items():
                if app_label in allowed_apps:
                    filtered_dict[app_label] = app_data
                    
            return filtered_dict
            
        elif user_role == 'bodeguero':
            # Bodegueros solo ven productos e inventario
            allowed_apps = ['productos', 'inventario']
            filtered_dict = {}
            
            for app_label, app_data in app_dict.items():
                if app_label in allowed_apps:
                    filtered_dict[app_label] = app_data
                    
            return filtered_dict
            
        return {}

# Instancia del AdminSite personalizado
role_based_admin_site = RoleBasedAdminSite(name='role_based_admin')

# Función para registrar automáticamente todos los modelos existentes
def register_all_models():
    """
    Registrar todos los modelos en el AdminSite personalizado
    """
    from django.apps import apps
    from django.contrib.admin.sites import site
    
    # Apps que queremos incluir en el admin personalizado
    target_apps = [
        'usuarios', 'roles', 'productos', 'inventario', 
        'ventas', 'clientes', 'proveedores', 'solicitudes_compra'
    ]
    
    for app_config in apps.get_app_configs():
        if app_config.label in target_apps:
            for model in app_config.get_models():
                # Solo registrar si no está ya registrado
                if model not in role_based_admin_site._registry:
                    # Copiar la configuración del admin por defecto si existe
                    if model in site._registry:
                        admin_class = site._registry[model].__class__
                        role_based_admin_site.register(model, admin_class)
                    else:
                        role_based_admin_site.register(model)

# Registrar modelos automáticamente
register_all_models()