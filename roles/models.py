from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
