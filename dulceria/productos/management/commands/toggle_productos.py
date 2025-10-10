from django.core.management.base import BaseCommand
from productos.models import Producto

class Command(BaseCommand):
    help = 'Desactiva algunos productos para probar el filtro de inactivos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--activar',
            action='store_true',
            help='Activar productos en lugar de desactivar'
        )

    def handle(self, *args, **options):
        if options['activar']:
            # Activar todos los productos
            productos_inactivos = Producto.objects.filter(activo=False)
            count = productos_inactivos.update(activo=True)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Se activaron {count} productos')
            )
        else:
            # Desactivar algunos productos para prueba
            productos_para_desactivar = Producto.objects.filter(activo=True)[:3]
            
            if not productos_para_desactivar.exists():
                self.stdout.write(
                    self.style.WARNING('No hay productos activos para desactivar')
                )
                return
            
            count = 0
            for producto in productos_para_desactivar:
                producto.activo = False
                producto.save()
                count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Desactivado: {producto.nombre}')
                )
            
            self.stdout.write('')
            self.stdout.write(
                self.style.SUCCESS(f'Total desactivados: {count} productos')
            )
            self.stdout.write('')
            self.stdout.write('Ahora puedes probar el filtro "Inactivos" en:')
            self.stdout.write('http://localhost:8000/productos/')
            self.stdout.write('')
            self.stdout.write('Para reactivarlos usa: python manage.py toggle_productos --activar')