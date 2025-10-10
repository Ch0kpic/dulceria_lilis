# Base de Datos - Dulcería Lilis

## 📋 Información de la base de datos exportada

### 🎯 **Para presentación en laboratorio**

Esta base de datos contiene todos los datos de prueba necesarios para la demostración del sistema:

### 📊 **Contenido incluido:**
- ✅ **Roles de usuario** (Administrador, Vendedor, Comprador)
- ✅ **Usuarios de prueba** con contraseñas configuradas
- ✅ **Productos del catálogo** (30+ productos premium)
- ✅ **Proveedores** (6 proveedores con información completa)
- ✅ **Solicitudes de compra** (ejemplos para demostración)

### 👥 **Usuarios disponibles:**
| Usuario | Contraseña | Rol | Permisos |
|---------|------------|-----|----------|
| `admin` | `admin123` | Administrador | Acceso completo |
| `vendedor` | `vendedor123` | Vendedor | Ventas y clientes |
| `comprador` | `comprador123` | Comprador | Solicitudes de compra |

### 🗄️ **Estructura de tablas principales:**
- `usuarios_usuario` - Información de usuarios del sistema
- `productos_producto` - Catálogo de productos
- `proveedores_proveedor` - Base de datos de proveedores
- `solicitudes_compra_solicitudcompra` - Gestión de compras
- `inventario_inventario` - Control de stock
- `ventas_venta` - Registro de transacciones

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