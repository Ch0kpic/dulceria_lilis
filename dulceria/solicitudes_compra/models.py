from django.db import models
from django.contrib.auth import get_user_model
from productos.models import Producto
from proveedores.models import Proveedor

Usuario = get_user_model()

class SolicitudCompra(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    id_solicitud = models.AutoField(primary_key=True)
    numero_solicitud = models.CharField(max_length=20, unique=True, editable=False)
    usuario_solicitante = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='solicitudes_creadas')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_necesaria = models.DateField(help_text="Fecha en que se necesitan los productos")
    observaciones = models.TextField(blank=True, help_text="Observaciones adicionales")
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Campos de seguimiento
    usuario_aprobador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='solicitudes_aprobadas')
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.numero_solicitud:
            # Generar número de solicitud automático
            import datetime
            fecha = datetime.datetime.now()
            ultimo_numero = SolicitudCompra.objects.filter(
                numero_solicitud__startswith=f"SOL-{fecha.year}"
            ).count()
            self.numero_solicitud = f"SOL-{fecha.year}-{ultimo_numero + 1:04d}"
        super().save(*args, **kwargs)
    
    @property
    def total(self):
        """Alias para total_estimado para compatibilidad con templates"""
        return self.total_estimado
    
    def __str__(self):
        return f"{self.numero_solicitud} - {self.get_estado_display()}"
    
    class Meta:
        verbose_name = 'Solicitud de Compra'
        verbose_name_plural = 'Solicitudes de Compra'
        ordering = ['-fecha_solicitud']


class DetalleSolicitudCompra(models.Model):
    solicitud = models.ForeignKey(SolicitudCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad_solicitada = models.PositiveIntegerField()
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio estimado por unidad")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    observaciones = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad_solicitada * self.precio_estimado
        super().save(*args, **kwargs)
        
        # Actualizar total de la solicitud
        if self.solicitud_id:
            total = sum(
                detalle.subtotal for detalle in self.solicitud.detalles.all()
            )
            SolicitudCompra.objects.filter(id_solicitud=self.solicitud_id).update(
                total_estimado=total
            )
    
    def __str__(self):
        return f"{self.solicitud.numero_solicitud} - {self.producto.nombre}"
    
    class Meta:
        verbose_name = 'Detalle de Solicitud'
        verbose_name_plural = 'Detalles de Solicitud'
        unique_together = ['solicitud', 'producto']