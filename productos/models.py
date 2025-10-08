from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255)
    precio_referencia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
