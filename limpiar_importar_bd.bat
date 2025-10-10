@echo off
chcp 65001 >nul
echo ============================================
echo   LIMPIAR Y PREPARAR BASE DE DATOS
echo ============================================
echo.

REM Verificar que WAMP esté ejecutándose
echo [1/4] Verificando WAMP Server...
ping -n 1 localhost >nul 2>&1
if errorlevel 1 (
    echo ERROR: WAMP Server no está ejecutándose
    pause
    exit /b 1
)

echo [2/4] Eliminando base de datos existente (si existe)...
mysql -u root -p --execute="DROP DATABASE IF EXISTS dulceria_lilis;"

echo [3/4] Creando base de datos limpia...
mysql -u root -p --execute="CREATE DATABASE dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"

echo [4/4] Importando datos...
if exist "dulceria_lilis.sql" (
    mysql -u root -p dulceria_lilis < dulceria_lilis.sql
) else (
    echo ERROR: No se encuentra dulceria_lilis.sql
    pause
    exit /b 1
)

echo.
echo ==========================================
echo     BASE DE DATOS IMPORTADA EXITOSAMENTE
echo ==========================================
echo.
echo Accede a: http://localhost/phpmyadmin
echo Base de datos: dulceria_lilis
echo.
pause