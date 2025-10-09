from django.shortcuts import redirect
from django.urls import resolve
from django.contrib import messages

class RolePermissionMiddleware:
    """
    Middleware para controlar el acceso basado en roles
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código que se ejecuta para cada request antes de la vista
        
        # Solo aplicar en el admin
        if request.path.startswith('/admin/'):
            user = request.user
            
            if user.is_authenticated and not user.is_superuser:
                if hasattr(user, 'id_rol') and user.id_rol:
                    rol = user.id_rol
                    current_url = resolve(request.path_info)
                    
                    # Mapear URLs del admin con permisos
                    permissions_map = {
                        'ventas': rol.puede_ver_ventas,
                        'inventario': rol.puede_ver_inventario,
                        'clientes': rol.puede_ver_clientes,
                        'proveedores': rol.puede_ver_proveedores,
                        'productos': rol.puede_ver_productos,
                        'usuarios': rol.puede_ver_usuarios,
                    }
                    
                    # Verificar si está intentando acceder a una sección restringida
                    for app_name, has_permission in permissions_map.items():
                        if f'/{app_name}/' in request.path and not has_permission:
                            messages.error(request, f'No tienes permisos para acceder a {app_name.title()}')
                            return redirect('/admin/')
        
        response = self.get_response(request)
        
        # Código que se ejecuta para cada request después de la vista
        
        return response