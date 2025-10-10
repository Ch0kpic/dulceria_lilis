-- Script SQL para configurar MySQL - Dulcería Lili's
-- Ejecutar este script en phpMyAdmin o MySQL Workbench

-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS dulceria_lilis 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 2. Crear usuario específico para el proyecto
CREATE USER IF NOT EXISTS 'dulceria_user'@'localhost' IDENTIFIED BY 'dulceria_password123';

-- 3. Otorgar todos los privilegios al usuario en la base de datos
GRANT ALL PRIVILEGES ON dulceria_lilis.* TO 'dulceria_user'@'localhost';

-- 4. Aplicar cambios
FLUSH PRIVILEGES;

-- 5. Verificar que todo esté correctamente configurado
USE dulceria_lilis;
SHOW TABLES;

-- 6. Mostrar información del usuario creado
SELECT User, Host FROM mysql.user WHERE User = 'dulceria_user';

-- Nota: Después de ejecutar este script, usar los comandos Django:
-- python manage.py migrate
-- python manage.py loaddata fixtures_roles.json
-- python manage.py loaddata fixtures_usuarios.json
-- python manage.py loaddata fixtures_proveedores.json
-- python manage.py loaddata fixtures_productos_premium.json