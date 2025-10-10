@echo off
title Instalacion Automatica - Dulceria Lilis
color 0A

echo ================================================================
echo    INSTALACION AUTOMATICA - DULCERIA LILIS
echo    Sistema de Gestion con Django + MySQL
echo ================================================================
echo.

:: Verificar si Python esta instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no esta instalado
    echo    Descarga e instala Python 3.11+ desde: https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Python detectado
python --version

:: Verificar si WAMP esta ejecutandose
netstat -an | find ":3306" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: MySQL no esta ejecutandose
    echo    Asegurate de que WAMP este activo (icono verde)
    pause
    exit /b 1
)

echo ✅ MySQL detectado en puerto 3306

:: Crear entorno virtual
echo.
echo 📦 Creando entorno virtual...
python -m venv env
if %errorlevel% neq 0 (
    echo ❌ ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)

:: Activar entorno virtual
echo ✅ Activando entorno virtual...
call env\Scripts\activate.bat

:: Instalar dependencias
echo.
echo 📚 Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo la instalacion de dependencias
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas

:: Cambiar al directorio dulceria
cd dulceria

:: Configurar base de datos MySQL
echo.
echo 🗄️  Configurando base de datos MySQL...
python -c "
import mysql.connector
import sys
try:
    print('Conectando a MySQL...')
    conn = mysql.connector.connect(host='localhost', user='root', password='')
    cursor = conn.cursor()
    
    print('Creando base de datos dulceria_lilis...')
    cursor.execute('CREATE DATABASE IF NOT EXISTS dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
    
    print('Creando usuario dulceria_user...')
    cursor.execute('CREATE USER IF NOT EXISTS \"dulceria_user\"@\"localhost\" IDENTIFIED BY \"dulceria_password123\"')
    
    print('Asignando privilegios...')
    cursor.execute('GRANT ALL PRIVILEGES ON dulceria_lilis.* TO \"dulceria_user\"@\"localhost\"')
    cursor.execute('FLUSH PRIVILEGES')
    
    cursor.close()
    conn.close()
    print('✅ Base de datos configurada correctamente')
    
except Exception as e:
    print(f'❌ Error configurando MySQL: {e}')
    print('Verifica que WAMP este ejecutandose correctamente')
    sys.exit(1)
"

if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo la configuracion de MySQL
    pause
    exit /b 1
)

:: Aplicar migraciones
echo.
echo 🔄 Aplicando migraciones de Django...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo la migracion de Django
    pause
    exit /b 1
)

echo ✅ Migraciones aplicadas

:: Cargar datos iniciales
echo.
echo 📋 Cargando datos iniciales...

echo   - Cargando roles...
python manage.py loaddata fixtures_roles.json
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo carga de roles
    pause
    exit /b 1
)

echo   - Cargando usuarios...
python manage.py loaddata fixtures_usuarios.json
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo carga de usuarios
    pause
    exit /b 1
)

echo   - Cargando proveedores...
python manage.py loaddata fixtures_proveedores.json
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo carga de proveedores
    pause
    exit /b 1
)

echo   - Cargando productos...
python manage.py loaddata fixtures_productos.json
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo carga de productos
    pause
    exit /b 1
)

echo   - Cargando productos premium...
python manage.py loaddata fixtures_productos_premium.json
if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo carga de productos premium
    pause
    exit /b 1
)

echo ✅ Datos iniciales cargados

:: Verificar instalacion
echo.
echo 🔍 Verificando instalacion...
python manage.py shell -c "
from usuarios.models import Usuario
from productos.models import Producto
from roles.models import Rol
print(f'✅ Usuarios: {Usuario.objects.count()}')
print(f'✅ Productos: {Producto.objects.count()}')
print(f'✅ Roles: {Rol.objects.count()}')
"

echo.
echo ================================================================
echo    🎉 INSTALACION COMPLETADA EXITOSAMENTE
echo ================================================================
echo.
echo 🌐 Para iniciar el servidor ejecuta:
echo     python manage.py runserver
echo.
echo 🔗 Luego accede a: http://127.0.0.1:8000
echo.
echo 👥 Usuarios de prueba:
echo     admin     / admin123     (Administrador)
echo     vendedor  / vendedor123  (Vendedor)
echo     comprador / comprador123 (Comprador)
echo.
echo 🗄️  phpMyAdmin: http://localhost/phpmyadmin
echo     Base de datos: dulceria_lilis
echo.
echo ================================================================

pause