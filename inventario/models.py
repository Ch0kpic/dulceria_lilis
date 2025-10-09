from django.db import models
from django.core.exceptions import ValidationError

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField()
    ubicacion = models.CharField(max_length=150)
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)
    stock_minimo = models.IntegerField(default=5, help_text="Cantidad mínima en stock")
    stock_maximo = models.IntegerField(default=100, help_text="Cantidad máxima en stock")

    def clean(self):
        super().clean()
        if self.cantidad_actual < 0:
            raise ValidationError('La cantidad actual no puede ser negativa')
        
        if self.stock_minimo < 0:
            raise ValidationError('El stock mínimo no puede ser negativo')
            
        if self.stock_maximo <= self.stock_minimo:
            raise ValidationError('El stock máximo debe ser mayor que el stock mínimo')
            
        if self.cantidad_actual > self.stock_maximo:
            raise ValidationError(f'La cantidad actual ({self.cantidad_actual}) excede el stock máximo permitido ({self.stock_maximo})')

    def __str__(self):
        return f"{self.id_producto.nombre} - Stock: {self.cantidad_actual}"

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        unique_together = ('id_producto', 'ubicacion')
