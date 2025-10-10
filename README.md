# Sistema de Gestión - Dulcería Lilis 🍭

Sistema web desarrollado en Django para la gestión integral de una dulcería con inventario, ventas, compras y usuarios con roles específicos.

## ✨ Características

- **Gestión de Usuarios**: Sistema de roles (Administrador, Vendedor, Comprador)
- **Inventario**: Control completo de productos y stock
- **Ventas**: Registro y seguimiento de transacciones
- **Compras**: Solicitudes de compra con aprobación por roles
- **Proveedores**: Gestión de información de proveedores
- **Reportes**: Dashboard con métricas del negocio

## 🛠️ Tecnologías

- **Backend**: Django 5.2.7
- **Base de Datos**: MySQL 8.3.0 (PyMySQL)
- **Frontend**: Bootstrap 5 + JavaScript
- **Servidor**: WAMP Server

## 🚀 Instalación

### Prerrequisitos
- ✅ WAMP Server ejecutándose (ícono verde)
- ✅ Python 3.11+

### Instalación Automática
```bash
INSTALAR.bat
```

### Instalación Manual
```bash
# 1. Crear entorno virtual
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

# 2. Configurar MySQL
cd dulceria
python -c "
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='')
cursor = conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS dulceria_lilis CHARACTER SET utf8mb4')
cursor.execute('CREATE USER IF NOT EXISTS \"dulceria_user\"@\"localhost\" IDENTIFIED BY \"dulceria_password123\"')
cursor.execute('GRANT ALL PRIVILEGES ON dulceria_lilis.* TO \"dulceria_user\"@\"localhost\"')
cursor.execute('FLUSH PRIVILEGES')
print('MySQL configurado')
"

# 3. Migrar datos
python manage.py migrate
python manage.py loaddata fixtures_roles.json
python manage.py loaddata fixtures_usuarios.json
python manage.py loaddata fixtures_proveedores.json
python manage.py loaddata fixtures_productos.json
python manage.py loaddata fixtures_productos_premium.json

# 4. Iniciar servidor
python manage.py runserver
```

## 🔑 Acceso

- **Web**: http://127.0.0.1:8000
- **Admin**: http://127.0.0.1:8000/admin
- **phpMyAdmin**: http://localhost/phpmyadmin

### Usuarios de Prueba
- **admin** / **admin123** (Administrador)
- **vendedor** / **vendedor123** (Vendedor)
- **comprador** / **comprador123** (Comprador)

## 📊 Datos Incluidos

- **3 Usuarios** con roles específicos
- **30 Productos** (chocolates, dulces, regalos)
- **6 Proveedores** con información completa
- **5 Roles** con permisos configurados

## 📁 Estructura

```
dulceria_lilis/
├── dulceria/              # Django principal
│   ├── manage.py
│   ├── .env              # Configuración
│   ├── dulceria/         # Settings
│   ├── usuarios/         # Gestión usuarios
│   ├── productos/        # Catálogo
│   ├── inventario/       # Stock
│   ├── proveedores/      # Proveedores
│   ├── ventas/          # Ventas
│   └── templates/       # HTML
├── requirements.txt     # Dependencias
├── INSTALAR.bat        # Script instalación
└── VERIFICAR_SISTEMA.bat # Verificación
```

## 🔐 Funcionalidades por Rol

**Administrador**: Acceso completo, gestión usuarios, reportes
**Vendedor**: Ventas, inventario, clientes
**Comprador**: Solicitudes compra, proveedores, stock

## ⚙️ Configuración MySQL

### Variables de entorno (.env)
```env
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=dulceria_lilis
DATABASE_USER=dulceria_user
DATABASE_PASSWORD=dulceria_password123
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

### Comandos útiles
```bash
# Verificar sistema
VERIFICAR_SISTEMA.bat

# Ver datos
python manage.py shell -c "
from usuarios.models import Usuario
from productos.models import Producto
print(f'Usuarios: {Usuario.objects.count()}')
print(f'Productos: {Producto.objects.count()}')
"

# Backup MySQL
mysqldump -u dulceria_user -p dulceria_lilis > backup.sql
```

## 🔧 Solución de Problemas

**Error MySQL**: Verificar WAMP activo, ejecutar `configurar_mysql.sql`
**Error dependencias**: `pip install -r requirements.txt`
**Error migraciones**: `python manage.py migrate --fake-initial`

## 📞 Contacto

- **Desarrollador**: Dylan
- **Repositorio**: https://github.com/Ch0kpic/dulceria_lilis
- **Estado**: ✅ Migrado a MySQL completamente

---

**Sistema listo para producción con MySQL** 🚀