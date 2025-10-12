-- Script para crear la base de datos de la Dulcería
-- Ejecutar en phpMyAdmin o cliente MySQL

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS dulceria_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos
USE dulceria_db;

-- Verificar que la base de datos se creó correctamente
SHOW DATABASES LIKE 'dulceria_db';

-- Mostrar información de la base de datos
SELECT 
    SCHEMA_NAME as 'Base de Datos',
    DEFAULT_CHARACTER_SET_NAME as 'Charset',
    DEFAULT_COLLATION_NAME as 'Collation'
FROM information_schema.SCHEMATA 
WHERE SCHEMA_NAME = 'dulceria_db';
