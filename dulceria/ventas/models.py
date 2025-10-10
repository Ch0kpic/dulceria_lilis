from django.db import models

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)
    id_cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)

    def __str__(self):
        return f"Venta {self.id_venta} - {self.fecha.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id_detalle} - Venta {self.id_venta.id_venta}"

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
