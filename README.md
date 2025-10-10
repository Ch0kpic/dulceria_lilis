# Sistema de Gestión - Dulcería Lilis

Sistema web desarrollado en Django para la gestión integral de una dulcería, incluyendo manejo de inventario, ventas, compras y usuarios con roles específicos.

## Características Principales

- **Gestión de Usuarios**: Sistema de roles (Administrador, Vendedor, Comprador)
- **Inventario**: Control completo de productos y stock
- **Ventas**: Registro y seguimiento de transacciones
- **Compras**: Solicitudes de compra con aprobación por roles
- **Proveedores**: Gestión de información de proveedores
- **Reportes**: Dashboard con métricas del negocio

## Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Base de Datos**: MySQL (compatible con WAMP)
- **Frontend**: Bootstrap 5 + JavaScript
- **Autenticación**: Sistema personalizado de Django

## Instalación Rápida para Laboratorio

### Prerrequisitos
- WAMP Server instalado y funcionando
- Python 3.11+ instalado
- Git instalado

### Pasos de Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Ch0kpic/dulceria_lilis.git
   cd dulceria_lilis
   ```

2. **Ejecutar instalación automática**:
   ```batch
   instalacion_rapida.bat
   ```

   Este script automáticamente:
   - Crea el entorno virtual
   - Instala las dependencias
   - Configura la base de datos MySQL
   - Ejecuta las migraciones
   - Carga datos de prueba
   - Crea superusuario (admin/admin123)

3. **Iniciar el servidor**:
   ```bash
   env\Scripts\activate
   cd dulceria
   python manage.py runserver
   ```

4. **Acceder al sistema**:
   - URL: http://127.0.0.1:8000
   - Admin: usuario `admin` / contraseña `admin123`

## Datos de Prueba Incluidos

### Usuarios Predefinidos
- **Administrador**: admin / admin123
- **Vendedor**: vendedor / vendedor123  
- **Comprador**: comprador / comprador123

### Catálogo de Productos
- 30 productos premium incluyendo:
  - Chocolates artesanales
  - Dulces importados
  - Regalos corporativos
  - Productos para eventos

### Proveedores
- 6 proveedores configurados con información completa
- Diferentes especialidades y términos de pago

## Estructura del Proyecto

```
dulceria_lilis/
├── dulceria/                 # Proyecto Django principal
│   ├── manage.py
│   ├── dulceria/            # Configuración del proyecto
│   ├── authentication/      # Autenticación personalizada
│   ├── usuarios/            # Gestión de usuarios
│   ├── roles/              # Sistema de roles
│   ├── productos/          # Catálogo de productos
│   ├── inventario/         # Control de stock
│   ├── proveedores/        # Gestión de proveedores
│   ├── solicitudes_compra/ # Sistema de compras
│   ├── ventas/             # Registro de ventas
│   ├── clientes/           # Información de clientes
│   └── templates/          # Plantillas HTML
├── env/                    # Entorno virtual Python
├── requirements.txt        # Dependencias del proyecto
├── .env.example           # Configuración de ejemplo
└── instalacion_rapida.bat # Script de instalación automática
```

## Funcionalidades por Rol

### Administrador
- Acceso completo al sistema
- Gestión de usuarios y roles
- Configuración del sistema
- Reportes y estadísticas

### Vendedor
- Registro de ventas
- Consulta de inventario
- Gestión de clientes
- Reportes de ventas

### Comprador
- Creación de solicitudes de compra
- Gestión de proveedores
- Seguimiento de pedidos
- Control de stock mínimo

## Base de Datos

El sistema utiliza MySQL y es compatible con WAMP Server. La configuración se realiza automáticamente durante la instalación.

### Configuración Manual (si es necesario)
```python
# En dulceria/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dulceria_lilis',
        'USER': 'root',
        'PASSWORD': '',  # Contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Comandos Útiles

### Cargar datos de prueba adicionales
```bash
python manage.py cargar_productos_premium
```

### Inicializar sistema completo
```bash
python manage.py inicializar_dulceria
```

### Crear superusuario adicional
```bash
python manage.py createsuperuser
```

## Solución de Problemas Comunes

### Error de conexión MySQL
1. Verificar que WAMP esté ejecutándose
2. Comprobar credenciales en `.env`
3. Asegurar que la base de datos `dulceria_lilis` exista

### Error de migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error de dependencias
```bash
pip install -r requirements.txt
```

## Contacto

Proyecto desarrollado para Dulcería Lilis
- Desarrollador: Dylan
- Repositorio: https://github.com/Ch0kpic/dulceria_lilis

## Licencia

Proyecto educativo - Todos los derechos reservados