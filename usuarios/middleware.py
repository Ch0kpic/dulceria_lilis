from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect

User = get_user_model()

class RolMiddleware:
    """
    Middleware para controlar el acceso al admin basado en roles
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Solo aplicar a URLs del admin
        if request.path.startswith('/admin/'):
            # Permitir acceso a login y logout
            if request.path in ['/admin/', '/admin/login/', '/admin/logout/']:
                return self.get_response(request)
            
            # Si el usuario está autenticado
            if request.user.is_authenticated:
                user_role = request.user.id_rol.nombre if hasattr(request.user, 'id_rol') else None
                
                # Bloquear acceso a ciertos modelos según el rol
                if user_role == 'Cliente':
                    # Los clientes no pueden acceder al admin
                    return HttpResponseForbidden("No tienes permisos para acceder a esta sección.")
                
                elif user_role == 'Vendedor':
                    # Los vendedores solo pueden ver productos e inventarios
                    allowed_paths = ['/admin/productos/', '/admin/inventarios/', '/admin/']
                    if not any(request.path.startswith(path) for path in allowed_paths):
                        return HttpResponseForbidden("No tienes permisos para acceder a esta sección.")
                
                elif user_role == 'Bodeguero':
                    # Los bodegueros pueden ver productos e inventarios
                    allowed_paths = ['/admin/productos/', '/admin/inventarios/', '/admin/']
                    if not any(request.path.startswith(path) for path in allowed_paths):
                        return HttpResponseForbidden("No tienes permisos para acceder a esta sección.")

        return self.get_response(request)
