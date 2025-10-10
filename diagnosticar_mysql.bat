@echo off
chcp 65001 >nul
echo ============================================
echo   FORZAR CONFIGURACIÓN MYSQL - DIAGNÓSTICO
echo ============================================
echo.

echo [1/8] Verificando WAMP/MySQL...
mysql --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: MySQL no está en el PATH o WAMP no está iniciado
    echo Soluciones:
    echo 1. Iniciar WAMP Server
    echo 2. Agregar MySQL al PATH: C:\wamp64\bin\mysql\mysql8.0.X\bin
    pause
    exit /b 1
)

echo [2/8] Verificando conexión MySQL...
mysql -u root -p --execute="SELECT 'MySQL conectado correctamente' AS status;"
if errorlevel 1 (
    echo ERROR: No se puede conectar a MySQL
    pause
    exit /b 1
)

echo [3/8] Eliminando BD existente...
mysql -u root -p --execute="DROP DATABASE IF EXISTS dulceria_lilis;"

echo [4/8] Creando nueva base de datos...
mysql -u root -p --execute="CREATE DATABASE dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"

echo [5/8] Verificando que se creó...
mysql -u root -p --execute="SHOW DATABASES LIKE 'dulceria_lilis';"

echo [6/8] Activando entorno virtual Django...
call env\Scripts\activate.bat

echo [7/8] Configurando Django para MySQL...
cd dulceria

REM Verificar configuración Django
python -c "
from django.conf import settings
import django
django.setup()
db = settings.DATABASES['default']
print(f'ENGINE: {db[\"ENGINE\"]}')
print(f'NAME: {db[\"NAME\"]}')
print(f'HOST: {db[\"HOST\"]}')
print(f'USER: {db[\"USER\"]}')
"

echo [8/8] Ejecutando migraciones...
python manage.py migrate --verbosity=2

echo.
echo ==========================================
echo     VERIFICACIÓN COMPLETADA
echo ==========================================
echo.
echo Ahora ve a phpMyAdmin:
echo http://localhost/phpmyadmin
echo.
echo Deberías ver la base de datos: dulceria_lilis
echo.
pause