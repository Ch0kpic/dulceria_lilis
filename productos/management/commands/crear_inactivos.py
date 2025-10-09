from django.core.management.base import BaseCommand
from productos.models import Producto
from decimal import Decimal

class Command(BaseCommand):
    help = 'Crea productos inactivos rápidamente para probar filtros'

    def handle(self, *args, **options):
        # Verificar productos existentes
        productos_inactivos = Producto.objects.filter(activo=False)
        
        if productos_inactivos.exists():
            self.stdout.write(self.style.SUCCESS(f'Ya existen {productos_inactivos.count()} productos inactivos:'))
            for p in productos_inactivos:
                self.stdout.write(f'  • {p.nombre}')
        else:
            # Crear productos inactivos
            productos_data = [
                {
                    'nombre': 'Producto Inactivo 1',
                    'descripcion': 'Este producto está desactivado para pruebas de filtro',
                    'precio_referencia': Decimal('1000.00'),
                    'activo': False
                },
                {
                    'nombre': 'Producto Inactivo 2',
                    'descripcion': 'Otro producto desactivado para testing',
                    'precio_referencia': Decimal('1500.00'),
                    'activo': False
                }
            ]
            
            for data in productos_data:
                producto = Producto.objects.create(**data)
                self.stdout.write(self.style.SUCCESS(f'✓ Creado: {producto.nombre}'))
            
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('¡Productos inactivos creados! Ahora puedes probar el filtro.'))