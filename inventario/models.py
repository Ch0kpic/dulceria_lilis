from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productos')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.sku})"

class AlertRule(models.Model):
    nombre = models.CharField(max_length=100)
    severidad = models.CharField(max_length=20, choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')])
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.severidad}"

class ProductAlertRule(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    regla_alerta = models.ForeignKey(AlertRule, on_delete=models.CASCADE)
    umbral_min = models.FloatField()
    umbral_max = models.FloatField()

    class Meta:
        unique_together = ('producto', 'regla_alerta')

    def __str__(self):
        return f"{self.producto} - {self.regla_alerta} ({self.umbral_min}/{self.umbral_max})"

class Organization(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Zone(models.Model):
    nombre = models.CharField(max_length=100)
    organizacion = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='zonas')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.organizacion})"

class Device(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='dispositivos')
    serial = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])

    def __str__(self):
        return f"{self.nombre} ({self.serial})"

class Measurement(models.Model):
    dispositivo = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='mediciones')
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dispositivo} - {self.valor} @ {self.fecha}"
