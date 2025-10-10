from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from roles.models import Rol

Usuario = get_user_model()

class Command(BaseCommand):
    help = 'Configura el rol de Comprador y los permisos de solicitudes de compra'
    
    def handle(self, *args, **options):
        self.stdout.write("🔧 Configurando rol Comprador...")
        
        # Buscar o crear el rol Comprador
        comprador_rol, created = Rol.objects.get_or_create(
            nombre='Comprador',
            defaults={
                'descripcion': 'Rol para gestionar solicitudes de compra y proveedores',
                'tipo': 'cliente',
                'puede_ver_solicitudes_compra': True,
                'puede_crear_solicitudes_compra': True,
                'puede_aprobar_solicitudes_compra': False,
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"✅ Rol 'Comprador' creado exitosamente")
            )
        else:
            # Actualizar permisos si ya existe
            comprador_rol.puede_ver_solicitudes_compra = True
            comprador_rol.puede_crear_solicitudes_compra = True
            comprador_rol.puede_aprobar_solicitudes_compra = False
            comprador_rol.save()
            self.stdout.write(
                self.style.SUCCESS(f"✅ Rol 'Comprador' actualizado")
            )
        
        # Buscar usuario dylan
        try:
            usuario_dylan = Usuario.objects.get(username='dylan')
            # Asignar el rol de Comprador
            usuario_dylan.id_rol = comprador_rol
            usuario_dylan.save()
            
            self.stdout.write(
                self.style.SUCCESS(f"✅ Usuario 'dylan' ahora tiene rol de 'Comprador'")
            )
            
            # Mostrar información del usuario
            self.stdout.write(f"📋 Información del usuario:")
            self.stdout.write(f"   - Username: {usuario_dylan.username}")
            self.stdout.write(f"   - Nombre: {getattr(usuario_dylan, 'nombre', 'N/A')}")
            self.stdout.write(f"   - Email: {usuario_dylan.email}")
            self.stdout.write(f"   - Rol: {usuario_dylan.id_rol.nombre if usuario_dylan.id_rol else 'Sin rol'}")
            self.stdout.write(f"   - Activo: {usuario_dylan.is_active}")
            
            if usuario_dylan.id_rol:
                self.stdout.write(f"📋 Permisos del rol:")
                self.stdout.write(f"   - Puede ver solicitudes: {usuario_dylan.id_rol.puede_ver_solicitudes_compra}")
                self.stdout.write(f"   - Puede crear solicitudes: {usuario_dylan.id_rol.puede_crear_solicitudes_compra}")
                self.stdout.write(f"   - Puede aprobar solicitudes: {usuario_dylan.id_rol.puede_aprobar_solicitudes_compra}")
            
        except Usuario.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f"❌ Usuario 'dylan' no encontrado")
            )
        
        # Crear rol Supervisor si no existe (para aprobar solicitudes)
        supervisor_rol, created = Rol.objects.get_or_create(
            nombre='Supervisor',
            defaults={
                'descripcion': 'Rol para supervisar y aprobar solicitudes de compra',
                'tipo': 'admin',
                'puede_ver_solicitudes_compra': True,
                'puede_crear_solicitudes_compra': True,
                'puede_aprobar_solicitudes_compra': True,
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"✅ Rol 'Supervisor' creado para aprobar solicitudes")
            )
        
        self.stdout.write(
            self.style.SUCCESS(f"🎉 Configuración completada exitosamente!")
        )