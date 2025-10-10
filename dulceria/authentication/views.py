from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from .forms import RegistroUsuarioForm

def login_view(request):
    # Si el usuario ya está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido {username}!")
                return redirect("dashboard")
            else:
                messages.error(request, "Credenciales incorrectas. Verifica tu usuario y contraseña.")
        else:
            messages.error(request, "Por favor verifica los datos ingresados.")
    else:
        form = AuthenticationForm()
    
    return render(request, "authentication/login.html", {"login_form": form})

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Cuenta creada exitosamente para: {username}. Ahora puedes iniciar sesión.")
            return redirect("login")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = RegistroUsuarioForm()
    return render(request, "authentication/registro.html", {"register_form": form})

@login_required
def dashboard_view(request):
    user = request.user
    
    # Importar modelos para las métricas
    from productos.models import Producto
    from proveedores.models import Proveedor
    from inventario.models import Inventario
    
    # Datos comunes para todos los dashboards
    productos_count = Producto.objects.count()
    proveedores_count = Proveedor.objects.count()
    # Contar productos con stock bajo (cantidad actual menor al stock mínimo)
    productos_bajo_stock = Inventario.objects.filter(cantidad_actual__lt=models.F('stock_minimo')).count()
    
    context = {
        'user': user,
        'rol_nombre': user.id_rol.nombre if user.id_rol else 'Sin rol asignado',
        'productos_count': productos_count,
        'proveedores_count': proveedores_count,
        'productos_bajo_stock': productos_bajo_stock,
    }
    
    # Determinar qué dashboard mostrar según el rol
    if user.id_rol:
        rol_tipo = user.id_rol.tipo
        
        # Dashboard para vendedores (vendedor y jefe_ventas)
        if rol_tipo in ['vendedor', 'jefe_ventas']:
            return render(request, "dashboards/vendedor.html", context)
        
        # Dashboard para compradores/bodegueros
        elif rol_tipo == 'bodeguero':
            return render(request, "dashboards/comprador.html", context)
        
        # Dashboard para administradores
        elif rol_tipo == 'admin':
            # El admin puede usar el dashboard completo
            return render(request, "dashboard.html", context)
    
    # Dashboard por defecto si no tiene rol específico
    return render(request, "dashboard.html", context)