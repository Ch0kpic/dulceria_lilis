from django.db import models
from productos.models import Producto
from proveedores.models import Proveedor

class ProductoProveedor(models.Model):
    id_producto_proveedor = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_acordado = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'producto_proveedor'
