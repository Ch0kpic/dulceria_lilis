from django.db import models

class Rol(models.Model):
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('jefe_ventas', 'Jefe de Ventas'),
        ('vendedor', 'Vendedor'),
        ('bodeguero', 'Bodeguero'),
        ('cliente', 'Cliente'),
        ('finanzas', 'Finanzas'),
    ]
    
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='cliente')
    
    # Permisos específicos
    puede_ver_ventas = models.BooleanField(default=False)
    puede_crear_ventas = models.BooleanField(default=False)
    puede_ver_inventario = models.BooleanField(default=False)
    puede_modificar_inventario = models.BooleanField(default=False)
    puede_ver_clientes = models.BooleanField(default=False)
    puede_crear_clientes = models.BooleanField(default=False)
    puede_ver_proveedores = models.BooleanField(default=False)
    puede_crear_proveedores = models.BooleanField(default=False)
    puede_ver_productos = models.BooleanField(default=False)
    puede_crear_productos = models.BooleanField(default=False)
    puede_ver_usuarios = models.BooleanField(default=False)
    puede_crear_usuarios = models.BooleanField(default=False)
    
    # Permisos de solicitudes de compra
    puede_ver_solicitudes_compra = models.BooleanField(default=False)
    puede_crear_solicitudes_compra = models.BooleanField(default=False)
    puede_aprobar_solicitudes_compra = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
