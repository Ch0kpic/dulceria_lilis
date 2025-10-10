from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.forms import inlineformset_factory
from .models import SolicitudCompra, DetalleSolicitudCompra
from .forms import SolicitudCompraForm, DetalleSolicitudCompraForm
from productos.models import Producto
from proveedores.models import Proveedor

@login_required
def lista_solicitudes(request):
    """Vista para mostrar lista de solicitudes de compra según rol"""
    solicitudes = SolicitudCompra.objects.all()
    
    # Filtrar según permisos del usuario
    if not request.user.is_superuser:
        if hasattr(request.user, 'id_rol') and request.user.id_rol:
            if not request.user.id_rol.puede_ver_solicitudes_compra:
                # Si no puede ver todas, solo sus propias solicitudes
                solicitudes = solicitudes.filter(usuario_solicitante=request.user)
    
    # Filtros
    estado = request.GET.get('estado')
    if estado:
        solicitudes = solicitudes.filter(estado=estado)
    
    prioridad = request.GET.get('prioridad')
    if prioridad:
        solicitudes = solicitudes.filter(prioridad=prioridad)
    
    search = request.GET.get('search')
    if search:
        solicitudes = solicitudes.filter(
            Q(numero_solicitud__icontains=search) |
            Q(observaciones__icontains=search) |
            Q(proveedor__nombre__icontains=search)
        )
    
    # Ordenamiento
    orden = request.GET.get('orden', '-fecha_solicitud')
    solicitudes = solicitudes.order_by(orden)
    
    # Paginación
    paginator = Paginator(solicitudes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'estados': SolicitudCompra.ESTADO_CHOICES,
        'prioridades': SolicitudCompra.PRIORIDAD_CHOICES,
        'search': search,
        'estado': estado,
        'prioridad': prioridad,
        'orden': orden,
    }
    return render(request, 'solicitudes_compra/lista.html', context)

@login_required
def crear_solicitud(request):
    """Vista para crear nueva solicitud de compra"""
    # Verificar permisos
    if not request.user.is_superuser:
        if not (hasattr(request.user, 'id_rol') and request.user.id_rol and 
                request.user.id_rol.puede_crear_solicitudes_compra):
            messages.error(request, 'No tienes permisos para crear solicitudes de compra.')
            return redirect('solicitudes_compra:lista')
    
    # Formset para detalles
    DetalleFormSet = inlineformset_factory(
        SolicitudCompra, 
        DetalleSolicitudCompra,
        form=DetalleSolicitudCompraForm,
        fk_name='solicitud',
        extra=1,
        can_delete=True
    )
    
    if request.method == 'POST':
        form = SolicitudCompraForm(request.POST)
        formset = DetalleFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario_solicitante = request.user
            solicitud.save()
            
            formset.instance = solicitud
            formset.save()
            
            messages.success(request, f'Solicitud {solicitud.numero_solicitud} creada exitosamente.')
            return redirect('solicitudes_compra:detalle', id_solicitud=solicitud.id_solicitud)
    else:
        form = SolicitudCompraForm()
        formset = DetalleFormSet()
    
    context = {
        'form': form,
        'formset': formset,
        'productos': Producto.objects.filter(activo=True),
        'proveedores': Proveedor.objects.all(),
    }
    return render(request, 'solicitudes_compra/crear.html', context)

@login_required
def detalle_solicitud(request, id_solicitud):
    """Vista para ver detalle de solicitud"""
    solicitud = get_object_or_404(SolicitudCompra, id_solicitud=id_solicitud)
    
    # Verificar permisos
    if not request.user.is_superuser:
        if hasattr(request.user, 'id_rol') and request.user.id_rol:
            if not request.user.id_rol.puede_ver_solicitudes_compra:
                # Solo puede ver sus propias solicitudes
                if solicitud.usuario_solicitante != request.user:
                    messages.error(request, 'No tienes permisos para ver esta solicitud.')
                    return redirect('solicitudes_compra:lista')
    
    context = {
        'solicitud': solicitud,
        'puede_aprobar': (request.user.is_superuser or 
                         (hasattr(request.user, 'id_rol') and request.user.id_rol and 
                          request.user.id_rol.puede_aprobar_solicitudes_compra))
    }
    return render(request, 'solicitudes_compra/detalle.html', context)

@login_required
def aprobar_solicitud(request, id_solicitud):
    """Vista para aprobar/rechazar solicitud"""
    solicitud = get_object_or_404(SolicitudCompra, id_solicitud=id_solicitud)
    
    # Verificar permisos
    if not request.user.is_superuser:
        if not (hasattr(request.user, 'id_rol') and request.user.id_rol and 
                request.user.id_rol.puede_aprobar_solicitudes_compra):
            return JsonResponse({'success': False, 'mensaje': 'Sin permisos'})
    
    if request.method == 'POST':
        accion = request.POST.get('accion')
        
        if accion == 'aprobar':
            solicitud.estado = 'aprobada'
            solicitud.usuario_aprobador = request.user
            from django.utils import timezone
            solicitud.fecha_aprobacion = timezone.now()
            mensaje = 'Solicitud aprobada exitosamente'
        elif accion == 'rechazar':
            solicitud.estado = 'rechazada'
            mensaje = 'Solicitud rechazada'
        
        solicitud.save()
        messages.success(request, mensaje)
        return redirect('solicitudes_compra:detalle', id_solicitud=solicitud.id_solicitud)
    
    return redirect('solicitudes_compra:detalle', id_solicitud=solicitud.id_solicitud)