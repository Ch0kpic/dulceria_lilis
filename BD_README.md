# Base de Datos MySQL - Dulcería Lilis 🗄️

## 📋 Información Actualizada - Migración a MySQL

### 🎯 **Configuración Actual del Sistema**

**✅ Estado**: Migrado completamente a **MySQL 8.3.0** con **PyMySQL**  
**✅ Servidor**: WAMP Server (localhost:3306)  
**✅ Base de datos**: `dulceria_lilis`  
**✅ Usuario**: `dulceria_user` / `dulceria_password123`  

### 📊 **Datos Migrados y Verificados:**
- ✅ **5 Roles** del sistema (Administrador, Vendedor, Comprador, etc.)
- ✅ **3 Usuarios** de prueba con contraseñas configuradas
- ✅ **30 Productos** del catálogo (regulares + premium)
- ✅ **6 Proveedores** con información completa
- ✅ **Estructura completa** de tablas Django

### 👥 **Usuarios Disponibles (Migrados a MySQL):**
| Usuario | Contraseña | Rol | Estado | Permisos |
|---------|------------|-----|---------|----------|
| `admin` | `admin123` | Administrador | ✅ Activo | Acceso completo al sistema |
| `vendedor` | `vendedor123` | Vendedor | ✅ Activo | Ventas, inventario, clientes |
| `comprador` | `comprador123` | Comprador | ✅ Activo | Solicitudes de compra, proveedores |

### 🗄️ **Estructura MySQL Actual:**
```sql
-- Tablas principales migradas:
auth_user                     -- Usuarios Django (3 registros)
usuarios_usuario              -- Usuarios personalizados (3 registros)  
roles_rol                     -- Roles del sistema (5 registros)
productos_producto            -- Catálogo productos (30 registros)
productos_categoria           -- Categorías de productos
proveedores_proveedor         -- Proveedores (6 registros)
inventario_inventario         -- Control de stock
solicitudes_compra_*          -- Sistema de compras
ventas_venta                  -- Registro de ventas
clientes_cliente              -- Base de clientes
```

## 🚀 **Instrucciones de uso en laboratorio:**

### **Opción A: Importación automática**
```batch
1. Asegurar que WAMP Server esté ejecutándose (ícono verde)
2. Ejecutar: importar_bd.bat
3. Seguir las instrucciones en pantalla
```

### **Opción B: Importación manual**
```bash
1. Abrir phpMyAdmin: http://localhost/phpmyadmin
2. Crear base de datos: dulceria_lilis
3. Seleccionar base de datos creada
4. Ir a "Importar"
5. Seleccionar archivo: dulceria_lilis.sql
6. Hacer clic en "Continuar"
```

### **Verificación:**
```bash
1. Ir a phpMyAdmin
2. Seleccionar base de datos dulceria_lilis
3. Verificar que existan las tablas
4. Revisar datos en tabla usuarios_usuario
```

### **Iniciar sistema Django:**
```bash
cd dulceria
python manage.py runserver
# Acceder a: http://127.0.0.1:8000
```

## 🎯 **Para la demostración:**

1. **Login como admin:** Mostrar panel administrativo completo
2. **Login como comprador:** Demostrar creación de solicitudes de compra
3. **Login como vendedor:** Mostrar gestión de ventas
4. **phpMyAdmin:** Mostrar tablas y datos en tiempo real

## 📝 **Notas importantes:**
- La base de datos usa codificación `utf8mb4` para caracteres especiales
- Todas las contraseñas están hasheadas correctamente
- Los datos incluyen fechas realistas para la demostración
- Compatible con WAMP Server configuración por defecto