@echo off
echo ============================================
echo    DULCERIA LILIS - INSTALACION RAPIDA
echo ============================================
echo.

REM Activar entorno virtual
echo [1/6] Activando entorno virtual...
call env\Scripts\activate
if %errorlevel% neq 0 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)

REM Instalar dependencias
echo [2/6] Instalando dependencias de Python...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

REM Crear migraciones
echo [3/6] Creando migraciones de base de datos...
python manage.py makemigrations
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Problemas con las migraciones
    pause
    exit /b 1
)

REM Cargar datos de prueba
echo [4/6] Cargando datos de ejemplo...
python manage.py inicializar_dulceria
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron cargar los datos
    pause
    exit /b 1
)

REM Configurar usuario comprador
echo [5/6] Configurando usuario comprador...
python manage.py configurar_comprador
if %errorlevel% neq 0 (
    echo ERROR: No se pudo configurar el usuario
    pause
    exit /b 1
)

REM Crear superusuario (opcional)
echo [6/6] Creando superusuario...
echo Creando superusuario 'admin' con password 'admin123'
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@dulceria.com', 'admin123') if not User.objects.filter(username='admin').exists() else None | python manage.py shell

echo.
echo ==========================================
echo    INSTALACION COMPLETADA EXITOSAMENTE
echo ==========================================
echo.
echo Usuarios disponibles:
echo - Admin: admin / admin123
echo - Comprador: dylan / (password original)
echo.
echo Para iniciar el servidor ejecuta:
echo python manage.py runserver
echo.
pause