from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from roles.models import Rol

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea usuarios de prueba para el sistema'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creando usuarios de prueba...'))

        # Obtener o crear roles
        try:
            rol_admin = Rol.objects.get(tipo='admin')
            rol_jefe_ventas = Rol.objects.get(tipo='jefe_ventas')
            rol_vendedor = Rol.objects.get(tipo='vendedor')
            rol_bodeguero = Rol.objects.get(tipo='bodeguero')
            rol_cliente = Rol.objects.get(tipo='cliente')
        except Rol.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    'Error: Los roles no existen. Ejecuta primero: python manage.py loaddata fixtures_roles.json'
                )
            )
            return

        # Crear usuarios de prueba
        usuarios = [
            {
                'username': 'admin',
                'password': 'admin123',
                'nombre': 'Administrador Principal',
                'correo': 'admin@dulceria.com',
                'id_rol': rol_admin,
                'is_superuser': True,
                'is_staff': True,
            },
            {
                'username': 'jefe_ventas',
                'password': 'ventas123',
                'nombre': 'Carlos Rodríguez',
                'correo': 'carlos@dulceria.com',
                'id_rol': rol_jefe_ventas,
                'is_staff': True,
            },
            {
                'username': 'vendedor1',
                'password': 'venta123',
                'nombre': 'María González',
                'correo': 'maria@dulceria.com',
                'id_rol': rol_vendedor,
                'is_staff': True,
            },
            {
                'username': 'vendedor2',
                'password': 'venta123',
                'nombre': 'Pedro Silva',
                'correo': 'pedro@dulceria.com',
                'id_rol': rol_vendedor,
                'is_staff': True,
            },
            {
                'username': 'bodeguero',
                'password': 'bodega123',
                'nombre': 'Ana Martínez',
                'correo': 'ana@dulceria.com',
                'id_rol': rol_bodeguero,
                'is_staff': True,
            },
            {
                'username': 'cliente1',
                'password': 'cliente123',
                'nombre': 'Juan Pérez',
                'correo': 'juan@email.com',
                'id_rol': rol_cliente,
                'is_staff': False,
            },
        ]

        created_count = 0
        for usuario_data in usuarios:
            username = usuario_data['username']
            
            # Verificar si el usuario ya existe
            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f'Usuario {username} ya existe, saltando...')
                )
                continue

            # Crear usuario
            user = User.objects.create_user(
                username=usuario_data['username'],
                password=usuario_data['password'],
                nombre=usuario_data['nombre'],
                correo=usuario_data['correo'],
                id_rol=usuario_data['id_rol'],
                is_superuser=usuario_data.get('is_superuser', False),
                is_staff=usuario_data.get('is_staff', False),
            )
            
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Usuario {username} creado exitosamente (Rol: {usuario_data["id_rol"].nombre})'
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n¡Proceso completado! Se crearon {created_count} usuarios.'
            )
        )
        
        self.stdout.write(
            self.style.SUCCESS('\nCredenciales de prueba:')
        )
        self.stdout.write('• Admin: admin / admin123')
        self.stdout.write('• Jefe Ventas: jefe_ventas / ventas123')
        self.stdout.write('• Vendedor 1: vendedor1 / venta123')
        self.stdout.write('• Vendedor 2: vendedor2 / venta123')
        self.stdout.write('• Bodeguero: bodeguero / bodega123')
        self.stdout.write('• Cliente: cliente1 / cliente123')