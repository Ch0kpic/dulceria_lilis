from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	ROLES = (
		('admin', 'Administrador'),
		('vendedor', 'Vendedor'),
		('operador', 'Operador'),
	)
	rol = models.CharField(max_length=20, choices=ROLES, default='vendedor')

	def __str__(self):
		return f"{self.username} ({self.get_rol_display()})"
