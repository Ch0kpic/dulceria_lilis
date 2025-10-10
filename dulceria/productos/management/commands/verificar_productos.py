from django.core.management.base import BaseCommand
from productos.models import Producto

class Command(BaseCommand):
    help = 'Verifica y crea productos inactivos para probar filtros'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Verificando productos en la base de datos...')
        
        # Contar productos por estado
        total_productos = Producto.objects.count()
        productos_activos = Producto.objects.filter(activo=True).count()
        productos_inactivos = Producto.objects.filter(activo=False).count()
        
        self.stdout.write(f'📊 RESUMEN ACTUAL:')
        self.stdout.write(f'   • Total productos: {total_productos}')
        self.stdout.write(f'   • Productos activos: {productos_activos}')
        self.stdout.write(f'   • Productos inactivos: {productos_inactivos}')
        
        # Si no hay productos inactivos, crear algunos
        if productos_inactivos == 0:
            self.stdout.write('')
            self.stdout.write(self.style.WARNING('⚠️  No hay productos inactivos. Creando algunos para pruebas...'))
            
            # Desactivar los primeros 2-3 productos activos si existen
            if productos_activos >= 2:
                productos_a_desactivar = Producto.objects.filter(activo=True)[:2]
                nombres_desactivados = []
                
                for producto in productos_a_desactivar:
                    producto.activo = False
                    producto.save()
                    nombres_desactivados.append(producto.nombre)
                    self.stdout.write(self.style.SUCCESS(f'   ✓ Desactivado: {producto.nombre}'))
                
                self.stdout.write('')
                self.stdout.write(self.style.SUCCESS(f'✅ Se desactivaron {len(nombres_desactivados)} productos'))
            else:
                # Crear productos inactivos desde cero
                productos_inactivos_data = [
                    {
                        'nombre': 'Producto de Prueba Inactivo 1',
                        'descripcion': 'Este producto está inactivo para probar filtros',
                        'precio_referencia': 1000.00,
                        'activo': False
                    },
                    {
                        'nombre': 'Producto de Prueba Inactivo 2', 
                        'descripcion': 'Otro producto inactivo para testing',
                        'precio_referencia': 1500.00,
                        'activo': False
                    }
                ]
                
                for producto_data in productos_inactivos_data:
                    producto = Producto.objects.create(**producto_data)
                    self.stdout.write(self.style.SUCCESS(f'   ✓ Creado: {producto.nombre}'))
                
                self.stdout.write('')
                self.stdout.write(self.style.SUCCESS(f'✅ Se crearon {len(productos_inactivos_data)} productos inactivos'))
        
        # Mostrar productos inactivos actuales
        self.stdout.write('')
        self.stdout.write('📋 PRODUCTOS INACTIVOS ACTUALES:')
        productos_inactivos_list = Producto.objects.filter(activo=False)
        
        if productos_inactivos_list.exists():
            for producto in productos_inactivos_list:
                self.stdout.write(f'   • ID {producto.id_producto}: {producto.nombre} (${producto.precio_referencia})')
        else:
            self.stdout.write(self.style.ERROR('   ❌ No hay productos inactivos'))
        
        self.stdout.write('')
        self.stdout.write('🧪 PRUEBA EL FILTRO:')
        self.stdout.write('1. Ve a: http://localhost:8000/productos/')
        self.stdout.write('2. En el filtro "Estado" selecciona "❌ Inactivos"')
        self.stdout.write('3. Deberías ver productos con fondo gris y etiqueta "(INACTIVO)"')
        
        # Mostrar comandos útiles
        self.stdout.write('')
        self.stdout.write('🔧 COMANDOS ÚTILES:')
        self.stdout.write('• Reactivar productos: python manage.py toggle_productos --activar')
        self.stdout.write('• Ver este reporte: python manage.py verificar_productos')