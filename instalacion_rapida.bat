@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

echo ============================================
echo    DULCERIA LILIS - INSTALACION RAPIDA
echo ============================================
echo.

REM Verificar que estamos en el directorio correcto
if not exist "requirements.txt" (
    echo ERROR: No se encontró requirements.txt
    echo Por favor ejecuta este script desde la carpeta raíz del proyecto
    echo Debe contener: README.md, requirements.txt, dulceria/, etc.
    echo.
    echo Directorio actual: %CD%
    pause
    exit /b 1
)

if not exist "dulceria" (
    echo ERROR: No se encontró la carpeta dulceria/
    echo Por favor ejecuta este script desde la carpeta raíz del proyecto
    pause
    exit /b 1
)

REM Verificar Python
echo [0/7] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no encontrado en el PATH
    echo Por favor instala Python 3.11+ y añádelo al PATH
    pause
    exit /b 1
)

REM Crear entorno virtual si no existe
echo [1/7] Verificando entorno virtual...
if not exist "env" (
    echo Creando entorno virtual...
    python -m venv env
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
)

REM Activar entorno virtual
echo [2/7] Activando entorno virtual...
call env\Scripts\activate
if %errorlevel% neq 0 (
    echo ERROR: No se pudo activar el entorno virtual
    echo Verifica que Python esté correctamente instalado
    pause
    exit /b 1
)

REM Instalar dependencias
echo [3/7] Instalando dependencias de Python...
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

REM Cambiar al directorio dulceria
echo [4/7] Configurando proyecto Django...
cd dulceria
if not exist "manage.py" (
    echo ERROR: No se encontró manage.py en dulceria/
    cd..
    pause
    exit /b 1
)

REM Crear migraciones
echo [5/7] Creando migraciones de base de datos...
python manage.py makemigrations 2>nul
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Problemas con las migraciones
    pause
    exit /b 1
)

REM Cargar datos de prueba
echo [6/7] Cargando datos de ejemplo...
python manage.py loaddata fixtures_roles.json 2>nul
python manage.py inicializar_dulceria
if %errorlevel% neq 0 (
    echo Advertencia: Algunos datos no se pudieron cargar, pero el sistema funcionará
)

REM Crear superusuario (opcional)
echo [7/7] Creando superusuario...
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dulceria.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@dulceria.com', 'admin123')
    print('Superusuario admin creado')
else:
    print('Superusuario admin ya existe')
"

cd..

echo.
echo ==========================================
echo    INSTALACION COMPLETADA EXITOSAMENTE
echo ==========================================
echo.
echo El sistema está listo para usar:
echo.
echo 1. Para iniciar el servidor:
echo    cd dulceria
echo    ..\env\Scripts\activate
echo    python manage.py runserver
echo.
echo 2. Acceder al sistema:
echo    URL: http://127.0.0.1:8000
echo    Usuario: admin / Contraseña: admin123
echo.
echo 3. Usuarios de prueba disponibles:
echo    - Vendedor: vendedor / vendedor123
echo    - Comprador: comprador / comprador123
echo.
pause