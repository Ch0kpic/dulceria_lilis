@echo off
chcp 65001 >nul
echo ============================================
echo   RESETEAR Y CONFIGURAR MYSQL - LABORATORIO
echo ============================================
echo.

echo [1/10] Activando entorno virtual...
if not exist "env\Scripts\activate.bat" (
    echo ERROR: Entorno virtual no encontrado
    echo Ejecuta primero: python -m venv env
    pause
    exit /b 1
)
call env\Scripts\activate.bat

echo [2/10] Verificando WAMP/MySQL...
mysql --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: MySQL no disponible
    echo - Iniciar WAMP Server
    echo - O agregar MySQL al PATH del sistema
    pause
    exit /b 1
)

echo [3/10] Eliminando base de datos SQLite anterior...
cd dulceria
if exist "db.sqlite3" (
    del db.sqlite3
    echo SQLite eliminado
)

echo [4/10] Eliminando archivos de migración...
for /d %%d in (*) do (
    if exist "%%d\migrations\0*.py" (
        del "%%d\migrations\0*.py"
        echo Migraciones eliminadas en %%d
    )
)

echo [5/10] Conectando a MySQL y limpiando BD...
mysql -u root -p --execute="DROP DATABASE IF EXISTS dulceria_lilis; CREATE DATABASE dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;" 2>nul

echo [6/10] Verificando configuración Django...
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dulceria.settings')
import django
django.setup()
from django.conf import settings
db = settings.DATABASES['default']
print(f'✓ ENGINE: {db[\"ENGINE\"]}')
print(f'✓ DATABASE: {db[\"NAME\"]}')  
print(f'✓ HOST: {db[\"HOST\"]}')
print(f'✓ USER: {db[\"USER\"]}')
"

echo [7/10] Creando migraciones nuevas...
python manage.py makemigrations

echo [8/10] Aplicando migraciones a MySQL...
python manage.py migrate

echo [9/10] Cargando datos de prueba...
python manage.py inicializar_dulceria

echo [10/10] Creando usuarios de prueba...
python manage.py crear_usuarios_prueba

echo.
echo ==========================================
echo      CONFIGURACIÓN MYSQL COMPLETADA
echo ==========================================
echo.
echo ✓ Base de datos MySQL: dulceria_lilis
echo ✓ phpMyAdmin: http://localhost/phpmyadmin
echo ✓ Django: python manage.py runserver
echo ✓ Sistema: http://127.0.0.1:8000
echo.
echo USUARIOS DISPONIBLES:
echo - admin / admin123 (Administrador)
echo - comprador / comprador123 (Solicitudes)
echo - vendedor / vendedor123 (Ventas)
echo.
pause