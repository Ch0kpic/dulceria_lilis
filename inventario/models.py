from django.db import models

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField()
    ubicacion = models.CharField(max_length=150)
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id_producto.nombre} - Stock: {self.cantidad_actual}"

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
