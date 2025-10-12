from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    descripcion = models.CharField(max_length=250, verbose_name="Descripción")
    precio_referencia = models.IntegerField(verbose_name="Precio de Referencia")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "producto"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio_referencia:,}"
