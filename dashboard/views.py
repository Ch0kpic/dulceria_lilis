from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from productos.models import Producto
from inventarios.models import Inventario
from .forms import ProductoForm, InventarioForm

def login_view(request):
    """Vista de login personalizada"""
    # Si el usuario ya está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'dashboard/new_login.html')

def logout_view(request):
    """Vista de logout"""
    logout(request)
    return redirect('dashboard:login')

@login_required
def home(request):
    """Dashboard principal"""
    user = request.user
    now = timezone.now()
    
    # Datos para el contexto
    context = {
        'user': user,
        'productos_count': Producto.objects.count(),
        'inventarios_count': Inventario.objects.count(),
        'today': now.date(),
        'now': now,
    }
    
    # Datos ficticios para proveedores y ventas (solo para administradores)
    if user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador'):
        context.update({
            'proveedores_count': 12,  # Ficticio
            'ventas_count': 156,      # Ficticio
        })
    
    return render(request, 'dashboard/home.html', context)

@login_required
def productos_view(request):
    """Vista de productos"""
    productos = Producto.objects.all().order_by('nombre')
    
    # Mock categories for filter
    class MockCategoria:
        def __init__(self, id, nombre):
            self.id = id
            self.nombre = nombre
    
    categorias = [
        MockCategoria(1, 'Chocolates'),
        MockCategoria(2, 'Caramelos'),
        MockCategoria(3, 'Galletas'),
        MockCategoria(4, 'Dulces'),
    ]
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'productos_count': productos.count(),
        'productos_activos': productos.count(),  # Assumiendo todos activos
        'productos_stock_bajo': 0,  # Mock data
        'productos_vencidos': 0,    # Mock data
        'user': request.user,
    }
    return render(request, 'dashboard/productos.html', context)

@login_required
def inventarios_view(request):
    """Vista de inventarios"""
    inventarios = Inventario.objects.select_related('id_producto').all()
    now = timezone.now()
    
    # Mock data para proveedores
    class MockProveedor:
        def __init__(self, id_proveedor, nombre):
            self.id_proveedor = id_proveedor
            self.nombre = nombre
    
    proveedores = [
        MockProveedor(1, 'Distribuidora Nacional'),
        MockProveedor(2, 'Dulces Premium SAC'),
        MockProveedor(3, 'Confitería del Norte'),
    ]
    
    context = {
        'inventarios': inventarios,
        'proveedores': proveedores,
        'total_productos': inventarios.count(),
        'stock_alto': 0,  # Calcular basado en lógica de stock
        'stock_medio': 0,
        'stock_bajo': 0,
        'today': now.date(),
        'user': request.user,
    }
    return render(request, 'dashboard/inventarios.html', context)

@login_required
def proveedores_view(request):
    """Vista ficticia de proveedores"""
    user = request.user
    
    # Solo administradores pueden acceder
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        raise PermissionDenied("No tienes permisos para acceder a esta sección")
    
    # Datos ficticios para proveedores
    class MockProveedor:
        def __init__(self, id_proveedor, nombre, contacto, telefono, email):
            self.id_proveedor = id_proveedor
            self.nombre = nombre
            self.contacto = contacto
            self.telefono = telefono
            self.email = email
    
    proveedores = [
        MockProveedor(1, 'Distribuidora Nacional', 'Juan Pérez', '123-456-7890', 'contacto@distrinacional.com'),
        MockProveedor(2, 'Dulces Premium SAC', 'María García', '098-765-4321', 'ventas@dulcespremium.com'),
        MockProveedor(3, 'Confitería del Norte', 'Carlos López', '555-123-4567', 'info@confiterianorte.com'),
    ]
    
    # Productos disponibles para asociar con proveedores
    productos_disponibles = Producto.objects.all()
    
    context = {
        'proveedores': proveedores,
        'productos_disponibles': productos_disponibles,
        'proveedores_count': len(proveedores),
        'proveedores_activos': len(proveedores),
        'productos_proveedor': productos_disponibles.count(),
        'ordenes_pendientes': 0,
        'user': request.user,
    }
    return render(request, 'dashboard/proveedores.html', context)

@login_required
def ventas_view(request):
    """Vista ficticia de ventas"""
    user = request.user
    
    # Solo administradores pueden acceder
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        raise PermissionDenied("No tienes permisos para acceder a esta sección")
    
    # Datos ficticios
    ventas = [
        {'id': 1, 'fecha': '2025-01-15', 'cliente': 'Cliente A', 'total': 50000, 'estado': 'Completada'},
        {'id': 2, 'fecha': '2025-01-14', 'cliente': 'Cliente B', 'total': 75000, 'estado': 'Pendiente'},
        {'id': 3, 'fecha': '2025-01-13', 'cliente': 'Cliente C', 'total': 30000, 'estado': 'Completada'},
    ]
    
    context = {
        'ventas': ventas,
        'user': request.user,
    }
    return render(request, 'dashboard/ventas.html', context)

@login_required
def agregar_producto(request):
    """Vista para agregar un nuevo producto"""
    user = request.user
    
    # Verificar permisos
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre in ['Administrador', 'Bodeguero'])):
        messages.error(request, 'No tienes permisos para agregar productos')
        return redirect('dashboard:productos')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" agregado exitosamente')
            return redirect('dashboard:productos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = ProductoForm()
    
    context = {
        'form': form,
        'user': user,
        'titulo': 'Agregar Nuevo Producto'
    }
    return render(request, 'dashboard/form_producto.html', context)

@login_required
def editar_producto(request, producto_id):
    """Vista para editar un producto existente"""
    user = request.user
    producto = get_object_or_404(Producto, id_producto=producto_id)
    
    # Solo administradores pueden editar
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        messages.error(request, 'No tienes permisos para editar productos')
        return redirect('dashboard:productos')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('dashboard:productos')
    else:
        form = ProductoForm(instance=producto)
    
    context = {
        'form': form,
        'user': user,
        'titulo': f'Editar Producto: {producto.nombre}',
        'producto': producto
    }
    return render(request, 'dashboard/form_producto.html', context)

@login_required
def agregar_inventario(request):
    """Vista para agregar un nuevo inventario"""
    user = request.user
    
    # Solo administradores pueden agregar inventarios
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        messages.error(request, 'Solo los administradores pueden agregar inventarios')
        return redirect('dashboard:inventarios')
    
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventario agregado exitosamente')
            return redirect('dashboard:inventarios')
    else:
        form = InventarioForm()
    
    context = {
        'form': form,
        'user': user,
        'titulo': 'Agregar Nuevo Inventario'
    }
    return render(request, 'dashboard/form_inventario.html', context)

@login_required
def editar_inventario(request, inventario_id):
    """Vista para editar un inventario existente"""
    user = request.user
    inventario = get_object_or_404(Inventario, id_inventario=inventario_id)
    
    # Solo administradores pueden editar
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        messages.error(request, 'No tienes permisos para editar inventarios')
        return redirect('dashboard:inventarios')
    
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventario actualizado exitosamente')
            return redirect('dashboard:inventarios')
    else:
        form = InventarioForm(instance=inventario)
    
    context = {
        'form': form,
        'user': user,
        'titulo': f'Editar Inventario: {inventario.id_producto.nombre}',
        'inventario': inventario
    }
    return render(request, 'dashboard/form_inventario.html', context)

def forgot_password_view(request):
    """Vista para recuperación de contraseña"""
    if request.method == 'POST':
        email = request.POST.get('email')
        # Aquí implementarías la lógica de envío de email
        messages.success(request, 'Se han enviado las instrucciones de recuperación a tu email')
        return redirect('dashboard:login')
    
    return render(request, 'dashboard/forgot_password.html')

def reset_password_view(request):
    """Vista para resetear contraseña"""
    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password == password_confirm:
            # Aquí implementarías la lógica de cambio de contraseña
            messages.success(request, 'Contraseña cambiada exitosamente')
            return redirect('dashboard:login')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    
    return render(request, 'dashboard/reset_password.html')

@login_required
def usuarios_view(request):
    """Vista de gestión de usuarios"""
    user = request.user
    
    # Solo administradores pueden gestionar usuarios
    if not (user.is_superuser or (hasattr(user, 'id_rol') and user.id_rol.nombre == 'Administrador')):
        raise PermissionDenied("No tienes permisos para gestionar usuarios")
    
    # Usar el modelo de Usuario personalizado
    from usuarios.models import Usuario
    from roles.models import Rol
    usuarios = Usuario.objects.select_related('id_rol').all()
    roles = Rol.objects.all()
    
    context = {
        'usuarios': usuarios,
        'roles': roles,
        'usuarios_count': usuarios.count(),
        'usuarios_activos': usuarios.filter(is_active=True).count(),
        'usuarios_inactivos': usuarios.filter(is_active=False).count(),
        'nuevos_usuarios': 0,  # Mock data
        'user': request.user,
    }
    return render(request, 'dashboard/usuarios.html', context)