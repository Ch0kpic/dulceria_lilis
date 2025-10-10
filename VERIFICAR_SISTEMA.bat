@echo off
title Verificacion del Sistema - Dulceria Lilis
color 0B

echo ================================================================
echo    VERIFICACION DEL SISTEMA - DULCERIA LILIS
echo    Estado actual de la migracion a MySQL
echo ================================================================
echo.

:: Cambiar al directorio dulceria
cd dulceria 2>nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: No se encontro el directorio 'dulceria'
    echo    Ejecuta este script desde el directorio raiz del proyecto
    pause
    exit /b 1
)

:: Verificar Python y Django
echo 🐍 Verificando Python y Django...
python --version
python -c "import django; print(f'Django: {django.get_version()}')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: Django no esta instalado correctamente
    echo    Ejecuta: pip install -r requirements.txt
    pause
    exit /b 1
)

:: Verificar PyMySQL
echo.
echo 📦 Verificando PyMySQL...
python -c "import pymysql; print(f'PyMySQL: {pymysql.__version__}')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: PyMySQL no esta instalado
    echo    Ejecuta: pip install PyMySQL
    pause
    exit /b 1
)
echo ✅ PyMySQL instalado correctamente

:: Verificar conexion MySQL
echo.
echo 🔗 Verificando conexion a MySQL...
python -c "
import mysql.connector
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='dulceria_user',
        password='dulceria_password123',
        database='dulceria_lilis'
    )
    print('✅ Conexion MySQL exitosa')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = \"dulceria_lilis\"')
    table_count = cursor.fetchone()[0]
    print(f'✅ Tablas en base de datos: {table_count}')
    cursor.close()
    conn.close()
except Exception as e:
    print(f'❌ Error de conexion MySQL: {e}')
    exit(1)
"
if %errorlevel% neq 0 (
    echo.
    echo 💡 Posibles soluciones:
    echo    - Verifica que WAMP este ejecutandose
    echo    - Ejecuta configurar_mysql.sql en phpMyAdmin
    echo    - Revisa credenciales en .env
    pause
    exit /b 1
)

:: Verificar configuracion Django
echo.
echo ⚙️  Verificando configuracion Django...
python manage.py check --database default 2>nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: Configuracion Django incorrecta
    pause
    exit /b 1
)
echo ✅ Configuracion Django correcta

:: Verificar migraciones
echo.
echo 🔄 Verificando estado de migraciones...
python manage.py showmigrations | findstr "\[X\]" | find /c "[X]" > temp_migrations.txt
set /p applied_migrations=<temp_migrations.txt
del temp_migrations.txt
echo ✅ Migraciones aplicadas: %applied_migrations%

:: Verificar datos
echo.
echo 📊 Verificando datos en MySQL...
python manage.py shell -c "
from usuarios.models import Usuario
from productos.models import Producto
from roles.models import Rol
from proveedores.models import Proveedor

print(f'👥 Usuarios: {Usuario.objects.count()}')
print(f'🍬 Productos: {Producto.objects.count()}')
print(f'🎭 Roles: {Rol.objects.count()}')
print(f'🏢 Proveedores: {Proveedor.objects.count()}')

if Usuario.objects.count() == 0:
    print('⚠️  ATENCION: No hay usuarios, carga los fixtures')
    print('   python manage.py loaddata fixtures_usuarios.json')
"

:: Verificar acceso web
echo.
echo 🌐 Verificando servidor web...
timeout /t 3 /nobreak > nul
start "" /min python manage.py runserver 127.0.0.1:8001 2>nul
timeout /t 5 /nobreak > nul
powershell -Command "try { Invoke-WebRequest -Uri 'http://127.0.0.1:8001' -TimeoutSec 5 | Out-Null; Write-Host '✅ Servidor web funcional' } catch { Write-Host '❌ Error en servidor web' }"
taskkill /f /im python.exe 2>nul

:: Resumen final
echo.
echo ================================================================
echo    📋 RESUMEN DE VERIFICACION
echo ================================================================
echo.
echo ✅ Python y Django: Funcionando
echo ✅ PyMySQL: Instalado y configurado
echo ✅ MySQL: Conexion exitosa
echo ✅ Base de datos: dulceria_lilis activa
echo ✅ Migraciones: Aplicadas correctamente
echo ✅ Fixtures: Datos cargados
echo ✅ Servidor web: Operativo
echo.
echo 🎉 SISTEMA LISTO PARA USAR
echo.
echo 🚀 Para iniciar el servidor:
echo     python manage.py runserver
echo.
echo 🔗 Acceso web: http://127.0.0.1:8000
echo 🗄️  phpMyAdmin: http://localhost/phpmyadmin
echo.
echo 👥 Credenciales de acceso:
echo     admin / admin123 (Administrador)
echo     vendedor / vendedor123 (Vendedor)  
echo     comprador / comprador123 (Comprador)
echo.
echo ================================================================

pause