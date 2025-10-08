from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    contacto = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    id_usuario_registro = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class ProductoProveedor(models.Model):
    id_producto_proveedor = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_acordado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_producto.nombre} - {self.id_proveedor.nombre}"

    class Meta:
        verbose_name = 'Producto Proveedor'
        verbose_name_plural = 'Productos Proveedores'
        unique_together = ('id_producto', 'id_proveedor')
