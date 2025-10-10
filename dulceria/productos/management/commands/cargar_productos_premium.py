from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from productos.models import Producto

class Command(BaseCommand):
    help = 'Carga productos premium en la base de datos'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Elimina todos los productos existentes antes de cargar los nuevos',
        )
    
    def handle(self, *args, **options):
        self.stdout.write("🍬 Cargando productos premium para Dulcería Lilis...")
        
        if options['clear']:
            with transaction.atomic():
                productos_eliminados = Producto.objects.all().count()
                Producto.objects.all().delete()
                self.stdout.write(
                    self.style.WARNING(f"🗑️  Se eliminaron {productos_eliminados} productos existentes")
                )
        
        try:
            with transaction.atomic():
                # Cargar productos básicos primero
                self.stdout.write("📦 Cargando productos básicos...")
                call_command('loaddata', 'fixtures_productos.json', verbosity=0)
                
                # Cargar productos premium
                self.stdout.write("✨ Cargando productos premium...")
                call_command('loaddata', 'fixtures_productos_premium.json', verbosity=0)
                
                # Mostrar estadísticas
                total_productos = Producto.objects.count()
                productos_activos = Producto.objects.filter(activo=True).count()
                
                self.stdout.write(
                    self.style.SUCCESS(f"✅ ¡Carga completada exitosamente!")
                )
                self.stdout.write(f"📊 Total de productos: {total_productos}")
                self.stdout.write(f"🟢 Productos activos: {productos_activos}")
                
                # Mostrar algunos productos de ejemplo
                self.stdout.write("\n🎯 Productos destacados cargados:")
                productos_premium = Producto.objects.filter(
                    precio_referencia__gte=10000
                ).order_by('-precio_referencia')[:3]
                
                for producto in productos_premium:
                    self.stdout.write(
                        f"   • {producto.nombre} - ${producto.precio_referencia}"
                    )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error al cargar productos: {str(e)}")
            )
            raise e
        
        self.stdout.write(
            self.style.SUCCESS("\n🎉 ¡Dulcería Lilis lista para vender!")
        )