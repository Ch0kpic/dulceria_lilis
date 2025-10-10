from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from productos.models import Producto
from proveedores.models import Proveedor
from roles.models import Rol

class Command(BaseCommand):
    help = 'Inicializa la dulcería con todos los datos de ejemplo'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--productos-only',
            action='store_true',
            help='Solo cargar productos, no otros datos',
        )
        parser.add_argument(
            '--clear-all',
            action='store_true',
            help='Elimina todos los datos antes de cargar',
        )
    
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_INFO("🍭 ===== INICIALIZANDO DULCERÍA LILIS ===== 🍭")
        )
        
        if options['clear_all']:
            self.stdout.write("🗑️  Limpiando base de datos...")
            with transaction.atomic():
                Producto.objects.all().delete()
                if not options['productos_only']:
                    Proveedor.objects.all().delete()
                    # No eliminamos roles porque pueden estar en uso
        
        try:
            # 1. Cargar roles (si no es solo productos)
            if not options['productos_only']:
                self.stdout.write("👥 Configurando roles de usuario...")
                try:
                    call_command('loaddata', 'fixtures_roles.json', verbosity=0)
                    self.stdout.write(
                        self.style.SUCCESS("   ✅ Roles cargados correctamente")
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"   ⚠️  Roles: {str(e)}")
                    )
            
            # 2. Cargar usuarios (si no es solo productos)
            if not options['productos_only']:
                self.stdout.write("👤 Cargando usuarios de prueba...")
                try:
                    call_command('loaddata', 'fixtures_usuarios.json', verbosity=0)
                    from usuarios.models import Usuario
                    usuarios_count = Usuario.objects.count()
                    self.stdout.write(
                        self.style.SUCCESS(f"   ✅ {usuarios_count} usuarios cargados")
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"   ⚠️  Usuarios: {str(e)}")
                    )
            
            # 3. Cargar proveedores (si no es solo productos)
            if not options['productos_only']:
                self.stdout.write("🚚 Cargando proveedores...")
                try:
                    call_command('loaddata', 'fixtures_proveedores.json', verbosity=0)
                    proveedores_count = Proveedor.objects.count()
                    self.stdout.write(
                        self.style.SUCCESS(f"   ✅ {proveedores_count} proveedores cargados")
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"   ⚠️  Proveedores: {str(e)}")
                    )
            
            # 4. Cargar productos básicos
            self.stdout.write("🍬 Cargando productos básicos...")
            try:
                call_command('loaddata', 'fixtures_productos.json', verbosity=0)
                productos_basicos = Producto.objects.count()
                self.stdout.write(
                    self.style.SUCCESS(f"   ✅ Productos básicos cargados")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f"   ⚠️  Productos básicos: {str(e)}")
                )
            
            # 5. Cargar productos premium
            self.stdout.write("✨ Cargando productos premium...")
            try:
                call_command('loaddata', 'fixtures_productos_premium.json', verbosity=0)
                self.stdout.write(
                    self.style.SUCCESS(f"   ✅ Productos premium cargados")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f"   ⚠️  Productos premium: {str(e)}")
                )
            
            # Estadísticas finales
            total_productos = Producto.objects.count()
            productos_activos = Producto.objects.filter(activo=True).count()
            
            self.stdout.write(
                self.style.SUCCESS("\n🎉 ¡INICIALIZACIÓN COMPLETADA!")
            )
            
            # Mostrar resumen
            self.stdout.write(f"\n📊 RESUMEN:")
            if not options['productos_only']:
                self.stdout.write(f"   👥 Roles: {Rol.objects.count()}")
                from usuarios.models import Usuario
                self.stdout.write(f"   👤 Usuarios: {Usuario.objects.count()}")
                self.stdout.write(f"   🚚 Proveedores: {Proveedor.objects.count()}")
            self.stdout.write(f"   🍬 Productos totales: {total_productos}")
            self.stdout.write(f"   🟢 Productos activos: {productos_activos}")
            
            # Productos por rango de precio
            self.stdout.write(f"\n💰 POR RANGO DE PRECIO:")
            economicos = Producto.objects.filter(precio_referencia__lt=2000).count()
            medios = Producto.objects.filter(
                precio_referencia__gte=2000, 
                precio_referencia__lt=5000
            ).count()
            premium = Producto.objects.filter(precio_referencia__gte=5000).count()
            
            self.stdout.write(f"   💚 Económicos (< $2,000): {economicos}")
            self.stdout.write(f"   💙 Medios ($2,000 - $5,000): {medios}")
            self.stdout.write(f"   💜 Premium (> $5,000): {premium}")
            
            # Top 3 más caros
            self.stdout.write(f"\n🏆 TOP 3 PRODUCTOS PREMIUM:")
            top_productos = Producto.objects.order_by('-precio_referencia')[:3]
            for i, producto in enumerate(top_productos, 1):
                self.stdout.write(
                    f"   {i}. {producto.nombre} - ${producto.precio_referencia:,.0f}"
                )
            
            self.stdout.write(
                self.style.HTTP_INFO(f"\n🎯 ¡Dulcería Lilis lista para operar!")
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error durante la inicialización: {str(e)}")
            )
            raise e