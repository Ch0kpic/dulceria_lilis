from django.db import models
from ventas.models import Venta
from productos.models import Producto

class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

    class Meta:
        db_table = 'detalle_venta'
