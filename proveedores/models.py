
from django.db import models
from inventario.models import Product

class Proveedor(models.Model):
	nombre = models.CharField(max_length=100)
	contacto = models.CharField(max_length=100, blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	direccion = models.TextField(blank=True)

	def __str__(self):
		return self.nombre

class ProductoProveedor(models.Model):
	producto = models.ForeignKey(Product, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	fecha_registro = models.DateField(auto_now_add=True)

	class Meta:
		unique_together = ('producto', 'proveedor')

	def __str__(self):
		return f"{self.producto} - {self.proveedor}"
