from django.contrib import admin
from .models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
