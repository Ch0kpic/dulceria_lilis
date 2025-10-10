@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

echo ============================================
echo   IMPORTAR BASE DE DATOS - DULCERÍA LILIS
echo ============================================
echo.

REM Verificar que WAMP esté ejecutándose
echo [1/5] Verificando WAMP Server...
ping -n 1 localhost >nul 2>&1
if errorlevel 1 (
    echo ERROR: WAMP Server no está ejecutándose
    echo Por favor inicia WAMP Server primero
    pause
    exit /b 1
)

REM Verificar que existe el archivo SQL
if not exist "dulceria_lilis.sql" (
    if not exist "dulceria_lilis_backup.sql" (
        echo ERROR: No se encuentra archivo de base de datos
        echo Busca: dulceria_lilis.sql o dulceria_lilis_backup.sql
        pause
        exit /b 1
    )
    set SQL_FILE=dulceria_lilis_backup.sql
) else (
    set SQL_FILE=dulceria_lilis.sql
)

echo Usando archivo: !SQL_FILE!

REM Crear base de datos
echo [2/5] Creando base de datos dulceria_lilis...
mysql -u root -p --execute="CREATE DATABASE IF NOT EXISTS dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
if errorlevel 1 (
    echo ERROR: No se pudo crear la base de datos
    echo Verifica que MySQL esté ejecutándose en WAMP
    pause
    exit /b 1
)

REM Importar datos
echo [3/5] Importando datos desde !SQL_FILE!...
mysql -u root -p dulceria_lilis < !SQL_FILE!
if errorlevel 1 (
    echo ERROR: No se pudieron importar los datos
    pause
    exit /b 1
)

REM Activar entorno virtual
echo [4/5] Configurando Django...
if not exist "env\Scripts\activate.bat" (
    echo ERROR: Entorno virtual no encontrado
    echo Ejecuta primero: python -m venv env
    pause
    exit /b 1
)

call env\Scripts\activate.bat

REM Verificar conexión Django
echo [5/5] Verificando conexión Django-MySQL...
cd dulceria
python manage.py showmigrations >nul 2>&1
if errorlevel 1 (
    echo ERROR: Django no puede conectarse a MySQL
    echo Verifica la configuración en .env
    pause
    exit /b 1
)

echo.
echo ==========================================
echo    IMPORTACIÓN COMPLETADA EXITOSAMENTE
echo ==========================================
echo.
echo La base de datos está lista:
echo.
echo 1. phpMyAdmin: http://localhost/phpmyadmin
echo    - Base de datos: dulceria_lilis
echo    - Usuario MySQL: root (sin contraseña)
echo.
echo 2. Sistema Django: 
echo    cd dulceria
echo    python manage.py runserver
echo    - URL: http://127.0.0.1:8000
echo.
echo 3. Usuarios disponibles:
echo    - admin / admin123
echo    - vendedor / vendedor123
echo    - comprador / comprador123
echo.
pause