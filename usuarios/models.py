from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    correo = models.EmailField(unique=True, blank=True)
    contrasena = models.CharField(max_length=255, blank=True)
    id_rol = models.ForeignKey('roles.Rol', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
