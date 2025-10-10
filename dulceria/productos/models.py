from django.db import models
from django.urls import reverse

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, help_text="Nombre del producto")
    descripcion = models.CharField(max_length=255, help_text="Descripción del producto")
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio de referencia del producto")
    activo = models.BooleanField(default=True, help_text="Si el producto está activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('productos:detalle', kwargs={'pk': self.pk})
    
    def get_stock_total(self):
        """Retorna el stock total del producto en todas las ubicaciones"""
        return sum(inv.cantidad_actual for inv in self.inventario_set.all())

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
