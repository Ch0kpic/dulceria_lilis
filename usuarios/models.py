from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Rol

class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    contrasena = models.CharField(max_length=250, verbose_name="Contraseña")
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")
    
    # Campos adicionales para AbstractUser
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['username', 'nombre']
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuario"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.id_rol.nombre})"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.correo
        if not self.email:
            self.email = self.correo
        super().save(*args, **kwargs)
