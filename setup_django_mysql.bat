@echo off
chcp 65001 >nul
echo ============================================
echo   CONFIGURACIÓN DJANGO + MYSQL DIRECTO
echo ============================================
echo.

echo [1/6] Activando entorno virtual...
call env\Scripts\activate.bat

echo [2/6] Creando base de datos en MySQL...
mysql -u root -p --execute="CREATE DATABASE IF NOT EXISTS dulceria_lilis CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"

echo [3/6] Ejecutando migraciones Django...
cd dulceria
python manage.py makemigrations
python manage.py migrate

echo [4/6] Cargando datos de ejemplo...
python manage.py inicializar_dulceria

echo [5/6] Creando usuarios de prueba...
python manage.py crear_usuarios_prueba

echo [6/6] Verificando instalación...
python manage.py check

echo.
echo ==========================================
echo     SISTEMA LISTO PARA USAR
echo ==========================================
echo.
echo Usuarios disponibles:
echo - admin / admin123
echo - vendedor / vendedor123  
echo - comprador / comprador123
echo.
echo Para iniciar:
echo python manage.py runserver
echo.
pause