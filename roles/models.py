from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Rol")
    descripcion = models.CharField(max_length=191, verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "rol"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
