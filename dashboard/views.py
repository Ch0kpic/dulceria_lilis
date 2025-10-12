from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.http import JsonResponse
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
    
    return render(request, 'dashboard/login.html')

def logout_view(request):
    """Vista de logout"""
    logout(request)
    return redirect('dashboard:login')

@login_required
def home(request):
    """Dashboard principal"""
    user = request.user
    
    # Datos para el contexto
    context = {
        'user': user,
        'productos_count': Producto.objects.count(),
        'inventarios_count': Inventario.objects.count(),
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
    context = {
        'productos': productos,
        'user': request.user,
    }
    return render(request, 'dashboard/productos.html', context)

@login_required
def inventarios_view(request):
    """Vista de inventarios"""
    inventarios = Inventario.objects.select_related('id_producto').all()
    context = {
        'inventarios': inventarios,
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
    
    # Datos ficticios
    proveedores = [
        {'id': 1, 'nombre': 'Proveedor A', 'contacto': 'contacto@proveedora.com', 'telefono': '123-456-7890'},
        {'id': 2, 'nombre': 'Proveedor B', 'contacto': 'contacto@proveedorb.com', 'telefono': '098-765-4321'},
        {'id': 3, 'nombre': 'Proveedor C', 'contacto': 'contacto@proveedorc.com', 'telefono': '555-123-4567'},
    ]
    
    context = {
        'proveedores': proveedores,
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