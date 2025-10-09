from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm
from inventario.models import Inventario

@login_required
def lista_productos(request):
    """Vista para mostrar la lista de productos con filtros y búsqueda"""
    productos = Producto.objects.all()
    
    # Filtro por estado activo
    activo = request.GET.get('activo')
    if activo == 'true':
        productos = productos.filter(activo=True)
    elif activo == 'false':
        productos = productos.filter(activo=False)
    
    # Filtro de búsqueda
    search = request.GET.get('search')
    if search and search not in ['None', 'null', '']:
        productos = productos.filter(
            Q(nombre__icontains=search) | 
            Q(descripcion__icontains=search)
        )
    
    # Filtro por rango de precio
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    if precio_min and precio_min.strip():
        productos = productos.filter(precio_referencia__gte=precio_min)
    if precio_max and precio_max.strip():
        productos = productos.filter(precio_referencia__lte=precio_max)
    
    # Ordenamiento
    orden = request.GET.get('orden', 'nombre')
    if orden in ['nombre', '-nombre', 'precio_referencia', '-precio_referencia', 'fecha_creacion', '-fecha_creacion']:
        productos = productos.order_by(orden)
    
    # Paginación
    paginator = Paginator(productos, 10)  # 10 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search': search,
        'activo': activo,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'orden': orden,
    }
    return render(request, 'productos/lista.html', context)

@login_required
def detalle_producto(request, pk):
    """Vista para mostrar detalles de un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    inventarios = Inventario.objects.filter(id_producto=producto)
    
    context = {
        'producto': producto,
        'inventarios': inventarios,
    }
    return render(request, 'productos/detalle.html', context)

@login_required
def crear_producto(request):
    """Vista para crear un nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
            return redirect('productos:detalle', pk=producto.pk)
    else:
        form = ProductoForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Producto',
        'boton': 'Crear Producto'
    }
    return render(request, 'productos/formulario.html', context)

@login_required
def editar_producto(request, pk):
    """Vista para editar un producto existente"""
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado exitosamente.')
            return redirect('productos:detalle', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    
    context = {
        'form': form,
        'producto': producto,
        'titulo': 'Editar Producto',
        'boton': 'Actualizar Producto'
    }
    return render(request, 'productos/formulario.html', context)

@login_required
def eliminar_producto(request, pk):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        nombre_producto = producto.nombre
        try:
            producto.delete()
            messages.success(request, f'Producto "{nombre_producto}" eliminado exitosamente.')
            return redirect('productos:lista')
        except Exception as e:
            messages.error(request, f'Error al eliminar el producto: {str(e)}')
    
    context = {
        'producto': producto,
    }
    return render(request, 'productos/confirmar_eliminacion.html', context)

@login_required
def toggle_activo(request, pk):
    """Vista AJAX para cambiar el estado activo de un producto"""
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        producto.activo = not producto.activo
        producto.save()
        
        return JsonResponse({
            'success': True,
            'activo': producto.activo,
            'mensaje': f'Producto {"activado" if producto.activo else "desactivado"} exitosamente.'
        })
    
    return JsonResponse({'success': False, 'mensaje': 'Método no permitido.'})
