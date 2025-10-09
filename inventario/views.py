from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Inventario
from .forms import InventarioForm
from productos.models import Producto

@login_required
def lista_inventario(request):
    """Vista para mostrar la lista de inventario con filtros y búsqueda"""
    inventarios = Inventario.objects.select_related('id_producto').all()
    
    # Filtro de búsqueda
    search = request.GET.get('search')
    if search:
        inventarios = inventarios.filter(
            Q(id_producto__nombre__icontains=search) | 
            Q(ubicacion__icontains=search)
        )
    
    # Filtro por ubicación
    ubicacion = request.GET.get('ubicacion')
    if ubicacion:
        inventarios = inventarios.filter(ubicacion__icontains=ubicacion)
    
    # Filtro por estado de stock
    stock_estado = request.GET.get('stock_estado')
    if stock_estado == 'bajo':
        inventarios = [inv for inv in inventarios if inv.cantidad_actual <= inv.stock_minimo]
    elif stock_estado == 'agotado':
        inventarios = inventarios.filter(cantidad_actual=0)
    elif stock_estado == 'normal':
        inventarios = [inv for inv in inventarios if inv.cantidad_actual > inv.stock_minimo]
    
    # Convertir de vuelta a QuerySet si es necesario
    if isinstance(inventarios, list):
        inventario_ids = [inv.id for inv in inventarios]
        inventarios = Inventario.objects.filter(id__in=inventario_ids).select_related('id_producto')
    
    # Ordenamiento
    orden = request.GET.get('orden', 'id_producto__nombre')
    if orden in ['id_producto__nombre', '-id_producto__nombre', 'cantidad_actual', '-cantidad_actual', 'ubicacion', '-ubicacion']:
        inventarios = inventarios.order_by(orden)
    
    # Paginación
    paginator = Paginator(inventarios, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search': search,
        'ubicacion': ubicacion,
        'stock_estado': stock_estado,
        'orden': orden,
    }
    return render(request, 'inventario/lista.html', context)

@login_required
def detalle_inventario(request, pk):
    """Vista para mostrar detalles de un inventario"""
    inventario = get_object_or_404(Inventario, pk=pk)
    
    context = {
        'inventario': inventario,
    }
    return render(request, 'inventario/detalle.html', context)

@login_required
def crear_inventario(request):
    """Vista para crear un nuevo registro de inventario"""
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            inventario = form.save()
            messages.success(request, f'Inventario para "{inventario.id_producto.nombre}" creado exitosamente.')
            return redirect('inventario:detalle', pk=inventario.pk)
    else:
        form = InventarioForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Registro de Inventario',
        'boton': 'Crear Inventario'
    }
    return render(request, 'inventario/formulario.html', context)

@login_required
def editar_inventario(request, pk):
    """Vista para editar un registro de inventario"""
    inventario = get_object_or_404(Inventario, pk=pk)
    
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            inventario = form.save()
            messages.success(request, f'Inventario para "{inventario.id_producto.nombre}" actualizado exitosamente.')
            return redirect('inventario:detalle', pk=inventario.pk)
    else:
        form = InventarioForm(instance=inventario)
    
    context = {
        'form': form,
        'inventario': inventario,
        'titulo': 'Editar Inventario',
        'boton': 'Actualizar Inventario'
    }
    return render(request, 'inventario/formulario.html', context)

@login_required
def eliminar_inventario(request, pk):
    """Vista para eliminar un registro de inventario"""
    inventario = get_object_or_404(Inventario, pk=pk)
    
    if request.method == 'POST':
        producto_nombre = inventario.id_producto.nombre
        try:
            inventario.delete()
            messages.success(request, f'Registro de inventario para "{producto_nombre}" eliminado exitosamente.')
            return redirect('inventario:lista')
        except Exception as e:
            messages.error(request, f'Error al eliminar el registro: {str(e)}')
    
    context = {
        'inventario': inventario,
    }
    return render(request, 'inventario/confirmar_eliminacion.html', context)

@login_required
def inventario_por_producto(request, producto_id):
    """Vista para mostrar todos los registros de inventario de un producto"""
    producto = get_object_or_404(Producto, pk=producto_id)
    inventarios = Inventario.objects.filter(id_producto=producto)
    
    context = {
        'producto': producto,
        'inventarios': inventarios,
    }
    return render(request, 'inventario/por_producto.html', context)
