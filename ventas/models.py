from django.db import models
from usuarios.models import Usuario
from dashboard.models import Cliente

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'venta'
