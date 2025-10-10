from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario
from productos.models import Producto
from inventario.models import Inventario

class Command(BaseCommand):
    help = 'Asigna permisos específicos a usuarios según su rol'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nombre de usuario')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = Usuario.objects.get(username=username)
            
            if user.id_rol and user.id_rol.tipo == 'bodeguero':
                # Permisos para productos
                producto_ct = ContentType.objects.get_for_model(Producto)
                producto_perms = Permission.objects.filter(content_type=producto_ct)
                
                # Permisos para inventario
                inventario_ct = ContentType.objects.get_for_model(Inventario)
                inventario_perms = Permission.objects.filter(content_type=inventario_ct)
                
                # Asignar todos los permisos
                all_perms = list(producto_perms) + list(inventario_perms)
                user.user_permissions.set(all_perms)
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Permisos de productos e inventario asignados a {username}'
                    )
                )
                
                # Mostrar permisos asignados
                for perm in all_perms:
                    self.stdout.write(f'  - {perm.name}')
                    
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f'El usuario {username} no tiene rol de bodeguero'
                    )
                )
                
        except Usuario.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Usuario {username} no encontrado')
            )