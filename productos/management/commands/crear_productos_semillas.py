from django.core.management.base import BaseCommand
from productos.models import Producto
from inventario.models import Inventario
from decimal import Decimal

class Command(BaseCommand):
    help = 'Crea productos de ejemplo para la dulcería'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creando productos de semillas para la dulcería...'))

        productos_data = [
            {
                'nombre': 'Alfajor de Dulce de Leche',
                'descripcion': 'Delicioso alfajor relleno con dulce de leche casero y cubierto de coco',
                'precio_referencia': Decimal('2500.00'),
                'activo': True
            },
            {
                'nombre': 'Chocolate con Almendras',
                'descripcion': 'Chocolate premium con almendras tostadas, ideal para regalo',
                'precio_referencia': Decimal('4500.00'),
                'activo': True
            },
            {
                'nombre': 'Caramelos de Miel',
                'descripcion': 'Caramelos artesanales elaborados con miel pura de abeja',
                'precio_referencia': Decimal('1200.00'),
                'activo': True
            },
            {
                'nombre': 'Bombones Surtidos',
                'descripcion': 'Caja de bombones variados con diferentes rellenos y sabores',
                'precio_referencia': Decimal('8900.00'),
                'activo': True
            },
            {
                'nombre': 'Turrones de Maní',
                'descripción': 'Turrones crujientes con maní tostado y miel',
                'precio_referencia': Decimal('3200.00'),
                'activo': True
            },
            {
                'nombre': 'Gomitas de Frutas',
                'descripcion': 'Gomitas suaves con sabores naturales de frutas',
                'precio_referencia': Decimal('800.00'),
                'activo': True
            },
            {
                'nombre': 'Paletas de Chocolate',
                'descripcion': 'Paletas de chocolate negro decoradas con sprinkles coloridos',
                'precio_referencia': Decimal('1800.00'),
                'activo': True
            },
            {
                'nombre': 'Marshmallows Gigantes',
                'descripcion': 'Marshmallows extra grandes perfectos para asar o comer solos',
                'precio_referencia': Decimal('1500.00'),
                'activo': True
            },
            {
                'nombre': 'Dulce de Leche Artesanal',
                'descripcion': 'Dulce de leche casero en frasco de vidrio de 500g',
                'precio_referencia': Decimal('5500.00'),
                'activo': True
            },
            {
                'nombre': 'Chupetes de Caramelo',
                'descripcion': 'Chupetes de caramelo duro con diferentes sabores frutales',
                'precio_referencia': Decimal('600.00'),
                'activo': True
            },
            {
                'nombre': 'Chocolatines Rellenos',
                'descripcion': 'Mini chocolates rellenos con crema de avellanas',
                'precio_referencia': Decimal('3800.00'),
                'activo': True
            },
            {
                'nombre': 'Chiclosos Masticables',
                'descripcion': 'Caramelos masticables con sabor a frutas tropicales',
                'precio_referencia': Decimal('900.00'),
                'activo': True
            },
            {
                'nombre': 'Barras de Cereal con Chocolate',
                'descripcion': 'Barras nutritivas de cereal cubiertas con chocolate con leche',
                'precio_referencia': Decimal('2200.00'),
                'activo': True
            },
            {
                'nombre': 'Mermelada de Frutilla Premium',
                'descripcion': 'Mermelada artesanal de frutillas con trozos de fruta',
                'precio_referencia': Decimal('4200.00'),
                'activo': True
            },
            {
                'nombre': 'Cookies de Chispas de Chocolate',
                'descripcion': 'Galletas caseras con chispas de chocolate belga',
                'precio_referencia': Decimal('2800.00'),
                'activo': True
            },
            {
                'nombre': 'Producto Descontinuado 1',
                'descripcion': 'Producto que ya no se produce - Solo para pruebas',
                'precio_referencia': Decimal('1000.00'),
                'activo': False
            },
            {
                'nombre': 'Producto Temporal Inactivo',
                'descripcion': 'Producto temporalmente fuera de stock',
                'precio_referencia': Decimal('1500.00'),
                'activo': False
            }
        ]

        # Datos de inventario para cada producto
        ubicaciones = [
            'Estante A1', 'Estante A2', 'Estante B1', 'Estante B2', 
            'Bodega Principal', 'Bodega Secundaria', 'Vitrina Principal',
            'Zona Refrigerada', 'Almacén General', 'Depósito'
        ]

        created_products = 0
        created_inventories = 0

        for i, producto_data in enumerate(productos_data):
            # Verificar si el producto ya existe
            if Producto.objects.filter(nombre=producto_data['nombre']).exists():
                self.stdout.write(
                    self.style.WARNING(f'El producto "{producto_data["nombre"]}" ya existe, saltando...')
                )
                continue

            # Crear producto
            producto = Producto.objects.create(**producto_data)
            created_products += 1
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Producto creado: {producto.nombre} - ${producto.precio_referencia}')
            )

            # Crear 1-3 registros de inventario por producto
            import random
            num_inventarios = random.randint(1, 3)
            ubicaciones_usadas = random.sample(ubicaciones, num_inventarios)

            for ubicacion in ubicaciones_usadas:
                # Generar cantidades realistas
                if 'chocolate' in producto.nombre.lower() or 'bombones' in producto.nombre.lower():
                    cantidad = random.randint(10, 50)  # Productos premium
                    stock_min = random.randint(3, 8)
                    stock_max = random.randint(30, 60)
                elif 'caramelos' in producto.nombre.lower() or 'gomitas' in producto.nombre.lower():
                    cantidad = random.randint(50, 200)  # Productos de mayor volumen
                    stock_min = random.randint(10, 20)
                    stock_max = random.randint(100, 250)
                else:
                    cantidad = random.randint(20, 100)  # Productos regulares
                    stock_min = random.randint(5, 15)
                    stock_max = random.randint(50, 120)

                inventario = Inventario.objects.create(
                    id_producto=producto,
                    cantidad_actual=cantidad,
                    ubicacion=ubicacion,
                    stock_minimo=stock_min,
                    stock_maximo=stock_max
                )
                created_inventories += 1

                # Mostrar estado del stock
                if cantidad <= stock_min:
                    estado = "STOCK BAJO"
                    color = self.style.WARNING
                elif cantidad >= stock_max * 0.8:
                    estado = "STOCK ALTO"
                    color = self.style.SUCCESS
                else:
                    estado = "STOCK NORMAL"
                    color = self.style.SUCCESS

                self.stdout.write(
                    color(f'   └─ Inventario: {ubicacion} - {cantidad} unidades ({estado})')
                )

        # Resumen final
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS(f'✓ RESUMEN DE CREACIÓN:'))
        self.stdout.write(self.style.SUCCESS(f'   • Productos creados: {created_products}'))
        self.stdout.write(self.style.SUCCESS(f'   • Inventarios creados: {created_inventories}'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write('')
        
        if created_products > 0:
            self.stdout.write(self.style.SUCCESS('🎉 ¡Datos de semillas creados exitosamente!'))
            self.stdout.write('')
            self.stdout.write('Ahora puedes:')
            self.stdout.write('• Ver productos en: http://localhost:8000/productos/')
            self.stdout.write('• Ver inventario en: http://localhost:8000/inventario/')
            self.stdout.write('• Acceder al admin en: http://localhost:8000/admin/')
        else:
            self.stdout.write(self.style.WARNING('Todos los productos ya existían en la base de datos.'))