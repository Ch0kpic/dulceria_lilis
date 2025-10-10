-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 10-10-2025 a las 04:19:04
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dulceria_lilis`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Empleados Limitados');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 36);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Usuario', 6, 'add_usuario'),
(22, 'Can change Usuario', 6, 'change_usuario'),
(23, 'Can delete Usuario', 6, 'delete_usuario'),
(24, 'Can view Usuario', 6, 'view_usuario'),
(25, 'Can add Rol', 7, 'add_rol'),
(26, 'Can change Rol', 7, 'change_rol'),
(27, 'Can delete Rol', 7, 'delete_rol'),
(28, 'Can view Rol', 7, 'view_rol'),
(29, 'Can add Cliente', 8, 'add_cliente'),
(30, 'Can change Cliente', 8, 'change_cliente'),
(31, 'Can delete Cliente', 8, 'delete_cliente'),
(32, 'Can view Cliente', 8, 'view_cliente'),
(33, 'Can add Producto', 9, 'add_producto'),
(34, 'Can change Producto', 9, 'change_producto'),
(35, 'Can delete Producto', 9, 'delete_producto'),
(36, 'Can view Producto', 9, 'view_producto'),
(37, 'Can add Inventario', 10, 'add_inventario'),
(38, 'Can change Inventario', 10, 'change_inventario'),
(39, 'Can delete Inventario', 10, 'delete_inventario'),
(40, 'Can view Inventario', 10, 'view_inventario'),
(41, 'Can add Proveedor', 11, 'add_proveedor'),
(42, 'Can change Proveedor', 11, 'change_proveedor'),
(43, 'Can delete Proveedor', 11, 'delete_proveedor'),
(44, 'Can view Proveedor', 11, 'view_proveedor'),
(45, 'Can add Producto Proveedor', 12, 'add_productoproveedor'),
(46, 'Can change Producto Proveedor', 12, 'change_productoproveedor'),
(47, 'Can delete Producto Proveedor', 12, 'delete_productoproveedor'),
(48, 'Can view Producto Proveedor', 12, 'view_productoproveedor'),
(49, 'Can add Venta', 13, 'add_venta'),
(50, 'Can change Venta', 13, 'change_venta'),
(51, 'Can delete Venta', 13, 'delete_venta'),
(52, 'Can view Venta', 13, 'view_venta'),
(53, 'Can add Detalle de Venta', 14, 'add_detalleventa'),
(54, 'Can change Detalle de Venta', 14, 'change_detalleventa'),
(55, 'Can delete Detalle de Venta', 14, 'delete_detalleventa'),
(56, 'Can view Detalle de Venta', 14, 'view_detalleventa'),
(57, 'Can add Solicitud de Compra', 15, 'add_solicitudcompra'),
(58, 'Can change Solicitud de Compra', 15, 'change_solicitudcompra'),
(59, 'Can delete Solicitud de Compra', 15, 'delete_solicitudcompra'),
(60, 'Can view Solicitud de Compra', 15, 'view_solicitudcompra'),
(61, 'Can add Detalle de Solicitud', 16, 'add_detallesolicitudcompra'),
(62, 'Can change Detalle de Solicitud', 16, 'change_detallesolicitudcompra'),
(63, 'Can delete Detalle de Solicitud', 16, 'delete_detallesolicitudcompra'),
(64, 'Can view Detalle de Solicitud', 16, 'view_detallesolicitudcompra');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes_cliente`
--

DROP TABLE IF EXISTS `clientes_cliente`;
CREATE TABLE IF NOT EXISTS `clientes_cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contacto` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `direccion` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-10-10 01:49:21.834074', '11', 'donas', 1, '[{\"added\": {}}]', 9, 1),
(2, '2025-10-10 01:49:34.467748', '12', 'donas', 1, '[{\"added\": {}}]', 9, 1),
(3, '2025-10-10 01:50:39.257588', '13', 'donas', 1, '[{\"added\": {}}]', 9, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'usuarios', 'usuario'),
(7, 'roles', 'rol'),
(8, 'clientes', 'cliente'),
(9, 'productos', 'producto'),
(10, 'inventario', 'inventario'),
(11, 'proveedores', 'proveedor'),
(12, 'proveedores', 'productoproveedor'),
(13, 'ventas', 'venta'),
(14, 'ventas', 'detalleventa'),
(15, 'solicitudes_compra', 'solicitudcompra'),
(16, 'solicitudes_compra', 'detallesolicitudcompra');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'roles', '0001_initial', '2025-10-10 00:52:49.957238'),
(2, 'contenttypes', '0001_initial', '2025-10-10 00:52:49.973179'),
(3, 'contenttypes', '0002_remove_content_type_name', '2025-10-10 00:52:49.996177'),
(4, 'auth', '0001_initial', '2025-10-10 00:52:50.072338'),
(5, 'auth', '0002_alter_permission_name_max_length', '2025-10-10 00:52:50.096575'),
(6, 'auth', '0003_alter_user_email_max_length', '2025-10-10 00:52:50.098579'),
(7, 'auth', '0004_alter_user_username_opts', '2025-10-10 00:52:50.098579'),
(8, 'auth', '0005_alter_user_last_login_null', '2025-10-10 00:52:50.104083'),
(9, 'auth', '0006_require_contenttypes_0002', '2025-10-10 00:52:50.104083'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2025-10-10 00:52:50.104083'),
(11, 'auth', '0008_alter_user_username_max_length', '2025-10-10 00:52:50.104083'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2025-10-10 00:52:50.104083'),
(13, 'auth', '0010_alter_group_name_max_length', '2025-10-10 00:52:50.120052'),
(14, 'auth', '0011_update_proxy_permissions', '2025-10-10 00:52:50.120052'),
(15, 'auth', '0012_alter_user_first_name_max_length', '2025-10-10 00:52:50.120052'),
(16, 'usuarios', '0001_initial', '2025-10-10 00:52:50.251086'),
(17, 'admin', '0001_initial', '2025-10-10 00:52:50.326743'),
(18, 'admin', '0002_logentry_remove_auto_add', '2025-10-10 00:52:50.326743'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-10 00:52:50.326743'),
(20, 'clientes', '0001_initial', '2025-10-10 00:52:50.326743'),
(21, 'productos', '0001_initial', '2025-10-10 00:52:50.342663'),
(22, 'inventario', '0001_initial', '2025-10-10 00:52:50.373878'),
(23, 'proveedores', '0001_initial', '2025-10-10 00:52:50.389874'),
(24, 'proveedores', '0002_initial', '2025-10-10 00:52:50.459091'),
(25, 'sessions', '0001_initial', '2025-10-10 00:52:50.469572'),
(26, 'ventas', '0001_initial', '2025-10-10 00:52:50.572855'),
(27, 'roles', '0002_rol_puede_aprobar_solicitudes_compra_and_more', '2025-10-10 01:59:08.846538'),
(28, 'solicitudes_compra', '0001_initial', '2025-10-10 01:59:09.023357');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1u4usb1wr5srixpa0zvjxx6qo0mzhlli', '.eJxVjEsOwjAMBe-SNYr6cXDMkn3PENlOSgookfpZIe4OlbqA7ZuZ9zKBtzWHbUlzmKK5mNacfjdhfaSyg3jncqtWa1nnSeyu2IMudqgxPa-H-3eQecnfGqProMUzN9oIATY4xk4VvcaExK5jL0TgnaADhZYSCNDo2ZPvuRfz_gDUVDeR:1v72fV:quh4XiVeHkToItuzOTOEyU6MxKmwdmiL_OnLHv3vI_Y', '2025-10-24 02:15:41.915122');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_inventario`
--

DROP TABLE IF EXISTS `inventario_inventario`;
CREATE TABLE IF NOT EXISTS `inventario_inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `cantidad_actual` int NOT NULL,
  `ubicacion` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_ultima_actualizacion` datetime(6) NOT NULL,
  `stock_minimo` int NOT NULL,
  `stock_maximo` int NOT NULL,
  `id_producto_id` int NOT NULL,
  PRIMARY KEY (`id_inventario`),
  UNIQUE KEY `inventario_inventario_id_producto_id_ubicacion_4af7c6f2_uniq` (`id_producto_id`,`ubicacion`),
  KEY `inventario_inventario_id_producto_id_08d16248` (`id_producto_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_producto`
--

DROP TABLE IF EXISTS `productos_producto`;
CREATE TABLE IF NOT EXISTS `productos_producto` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio_referencia` decimal(10,2) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) DEFAULT NULL,
  `fecha_actualizacion` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `productos_producto`
--

INSERT INTO `productos_producto` (`id_producto`, `nombre`, `descripcion`, `precio_referencia`, `activo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'Alfajor de Dulce de Leche', 'Delicioso alfajor de dulce de leche', 22500.00, 0, '2025-10-10 01:07:19.107049', '2025-10-10 01:17:13.548822'),
(2, 'Bombones Surtidos', 'Delicioso bombones surtidos', 8900.00, 0, '2025-10-10 01:07:19.107049', '2025-10-10 01:17:12.970128'),
(3, 'Caramelos de Miel', 'Delicioso caramelos de miel', 1200.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(4, 'Chocolate con Almendras', 'Delicioso chocolate con almendras', 4500.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(5, 'Chupetes de Caramelo', 'Delicioso chupetes de caramelo', 600.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(6, 'Dulce de Leche Artesanal', 'Delicioso dulce de leche artesanal', 5500.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(7, 'Gomitas de Frutas', 'Delicioso gomitas de frutas', 800.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(8, 'Marshmallows Gigantes', 'Delicioso marshmallows gigantes', 1500.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(9, 'Paletas de Chocolate', 'Delicioso paletas de chocolate', 1800.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(10, 'Turrones de Maní', 'Delicioso turrones de maní', 3200.00, 1, '2025-10-10 01:07:19.107049', '2025-10-10 01:07:19.107049'),
(11, 'donas', 'ricas donas', 1500.00, 1, '2025-10-10 01:49:21.833069', '2025-10-10 01:49:21.833069'),
(12, 'donas', 'ricas donas', 1500.00, 1, '2025-10-10 01:49:34.466738', '2025-10-10 01:49:34.466738'),
(13, 'donas', 'ricas donas', 1500.00, 1, '2025-10-10 01:50:39.256127', '2025-10-10 01:50:39.256127');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores_productoproveedor`
--

DROP TABLE IF EXISTS `proveedores_productoproveedor`;
CREATE TABLE IF NOT EXISTS `proveedores_productoproveedor` (
  `id_producto_proveedor` int NOT NULL AUTO_INCREMENT,
  `precio_acordado` decimal(10,2) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `id_producto_id` int NOT NULL,
  `id_proveedor_id` int NOT NULL,
  PRIMARY KEY (`id_producto_proveedor`),
  UNIQUE KEY `proveedores_productoprov_id_producto_id_id_provee_b850e2b8_uniq` (`id_producto_id`,`id_proveedor_id`),
  KEY `proveedores_productoproveedor_id_producto_id_60395eed` (`id_producto_id`),
  KEY `proveedores_productoproveedor_id_proveedor_id_86493972` (`id_proveedor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores_proveedor`
--

DROP TABLE IF EXISTS `proveedores_proveedor`;
CREATE TABLE IF NOT EXISTS `proveedores_proveedor` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contacto` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `direccion` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_registro` datetime(6) DEFAULT NULL,
  `id_usuario_registro_id` int NOT NULL,
  PRIMARY KEY (`id_proveedor`),
  KEY `proveedores_proveedor_id_usuario_registro_id_05dd72e4` (`id_usuario_registro_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles_rol`
--

DROP TABLE IF EXISTS `roles_rol`;
CREATE TABLE IF NOT EXISTS `roles_rol` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `puede_ver_ventas` tinyint(1) NOT NULL,
  `puede_crear_ventas` tinyint(1) NOT NULL,
  `puede_ver_inventario` tinyint(1) NOT NULL,
  `puede_modificar_inventario` tinyint(1) NOT NULL,
  `puede_ver_clientes` tinyint(1) NOT NULL,
  `puede_crear_clientes` tinyint(1) NOT NULL,
  `puede_ver_proveedores` tinyint(1) NOT NULL,
  `puede_crear_proveedores` tinyint(1) NOT NULL,
  `puede_ver_productos` tinyint(1) NOT NULL,
  `puede_crear_productos` tinyint(1) NOT NULL,
  `puede_ver_usuarios` tinyint(1) NOT NULL,
  `puede_crear_usuarios` tinyint(1) NOT NULL,
  `puede_aprobar_solicitudes_compra` tinyint(1) NOT NULL,
  `puede_crear_solicitudes_compra` tinyint(1) NOT NULL,
  `puede_ver_solicitudes_compra` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `roles_rol`
--

INSERT INTO `roles_rol` (`id_rol`, `nombre`, `descripcion`, `tipo`, `puede_ver_ventas`, `puede_crear_ventas`, `puede_ver_inventario`, `puede_modificar_inventario`, `puede_ver_clientes`, `puede_crear_clientes`, `puede_ver_proveedores`, `puede_crear_proveedores`, `puede_ver_productos`, `puede_crear_productos`, `puede_ver_usuarios`, `puede_crear_usuarios`, `puede_aprobar_solicitudes_compra`, `puede_crear_solicitudes_compra`, `puede_ver_solicitudes_compra`) VALUES
(1, 'Operador de Bodega', 'Maneja inventario y almacén', 'cliente', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 'Comprador', 'Realiza compras y gestiona proveedores', 'cliente', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
(3, 'Administrador', 'Acceso completo al sistema - puede ver y gestionar todo', 'cliente', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 'Empleado Limitado', 'Acceso solo a consulta de productos, sin permisos de edición', 'cliente', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 'Supervisor', 'Rol para supervisar y aprobar solicitudes de compra', 'admin', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes_compra_detallesolicitudcompra`
--

DROP TABLE IF EXISTS `solicitudes_compra_detallesolicitudcompra`;
CREATE TABLE IF NOT EXISTS `solicitudes_compra_detallesolicitudcompra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad_solicitada` int UNSIGNED NOT NULL,
  `precio_estimado` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `observaciones` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `producto_id` int NOT NULL,
  `solicitud_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `solicitudes_compra_detal_solicitud_id_producto_id_2a9b7cbd_uniq` (`solicitud_id`,`producto_id`),
  KEY `solicitudes_compra_detallesolicitudcompra_producto_id_5f0253a6` (`producto_id`),
  KEY `solicitudes_compra_detallesolicitudcompra_solicitud_id_98fb3946` (`solicitud_id`)
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes_compra_solicitudcompra`
--

DROP TABLE IF EXISTS `solicitudes_compra_solicitudcompra`;
CREATE TABLE IF NOT EXISTS `solicitudes_compra_solicitudcompra` (
  `id_solicitud` int NOT NULL AUTO_INCREMENT,
  `numero_solicitud` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prioridad` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_solicitud` datetime(6) NOT NULL,
  `fecha_necesaria` date NOT NULL,
  `observaciones` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_estimado` decimal(10,2) NOT NULL,
  `fecha_aprobacion` datetime(6) DEFAULT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `proveedor_id` int DEFAULT NULL,
  `usuario_aprobador_id` int DEFAULT NULL,
  `usuario_solicitante_id` int NOT NULL,
  PRIMARY KEY (`id_solicitud`),
  UNIQUE KEY `numero_solicitud` (`numero_solicitud`),
  KEY `solicitudes_compra_solicitudcompra_proveedor_id_af83c46f` (`proveedor_id`),
  KEY `solicitudes_compra_solicitudcompra_usuario_aprobador_id_b9a0066c` (`usuario_aprobador_id`),
  KEY `solicitudes_compra_solicitu_usuario_solicitante_id_886eef7d` (`usuario_solicitante_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_usuario`
--

DROP TABLE IF EXISTS `usuarios_usuario`;
CREATE TABLE IF NOT EXISTS `usuarios_usuario` (
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `correo` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contrasena` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_rol_id` int DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `correo` (`correo`),
  KEY `usuarios_usuario_id_rol_id_463daed5` (`id_rol_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios_usuario`
--

INSERT INTO `usuarios_usuario` (`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `id_usuario`, `nombre`, `correo`, `contrasena`, `id_rol_id`) VALUES
('pbkdf2_sha256$1000000$8ct45MT3Vrqd4VeI22oqKR$RsVtjF41UMTJWADN4NJsu8pLovTTFnXh/gkNGyDnsP8=', '2025-10-10 02:15:41.913117', 1, 'admin', '', '', 'admin@dulceria.com', 1, 1, '2025-10-10 01:07:02.466062', 1, 'Administrador', 'admin@dulceria.com', '', 3),
('pbkdf2_sha256$1000000$BlsXO5zRrqVXpTd7qoqqVm$1LQ58plch/MbDfZFP1U1PpBYDzZ2Dx2VS8E0wU/iS58=', '2025-10-10 02:15:13.071206', 0, 'dylan', '', '', 'dylan@dulceria.com', 0, 1, '2025-10-10 01:07:02.847730', 2, 'barraza', 'dylan@dulceria.com', '', 2),
('pbkdf2_sha256$1000000$IrKEi5bTl7vlz4uC1jwvXi$wgntrrMJNq9pIyhoMClt7TIwYtXaRhBLGlgVMFiLVUI=', '2025-10-10 01:22:17.106298', 0, 'pepe', '', '', 'pepe@dulceria.com', 0, 1, '2025-10-10 01:07:03.250846', 3, 'cardenas', 'pepe@dulceria.com', '', 1),
('pbkdf2_sha256$1000000$eDy9QDMyfjia23v26iSZoS$e/X5l46niK28dhGtTypPNEH9W5GA2S/fDBOoZQbiMMs=', '2025-10-10 01:13:31.298400', 0, 'luis', '', '', 'luis@gmail.com', 0, 1, '2025-10-10 01:13:24.550387', 4, 'perez', 'luis@gmail.com', '', 2),
('pbkdf2_sha256$1000000$QoXyIKwwWbrjpKgli3b86A$PtaPzZ4K+4VzUhpB+PqBu6miZc7iQohmdXd7rINhEEA=', '2025-10-10 01:51:44.161276', 0, 'empleado1', '', '', 'empleado1@dulceria.com', 1, 1, '2025-10-10 01:33:44.253274', 5, 'Juan Empleado', 'empleado1@dulceria.com', '', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_usuario_groups`
--

DROP TABLE IF EXISTS `usuarios_usuario_groups`;
CREATE TABLE IF NOT EXISTS `usuarios_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_groups_usuario_id_group_id_4ed5b09e_uniq` (`usuario_id`,`group_id`),
  KEY `usuarios_usuario_groups_usuario_id_7a34077f` (`usuario_id`),
  KEY `usuarios_usuario_groups_group_id_e77f6dcf` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios_usuario_groups`
--

INSERT INTO `usuarios_usuario_groups` (`id`, `usuario_id`, `group_id`) VALUES
(1, 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuarios_usuario_user_permissions`;
CREATE TABLE IF NOT EXISTS `usuarios_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_user_pe_usuario_id_permission_id_217cadcd_uniq` (`usuario_id`,`permission_id`),
  KEY `usuarios_usuario_user_permissions_usuario_id_60aeea80` (`usuario_id`),
  KEY `usuarios_usuario_user_permissions_permission_id_4e5c0f2f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_detalleventa`
--

DROP TABLE IF EXISTS `ventas_detalleventa`;
CREATE TABLE IF NOT EXISTS `ventas_detalleventa` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `id_producto_id` int NOT NULL,
  `id_venta_id` int NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `ventas_detalleventa_id_producto_id_901cf687` (`id_producto_id`),
  KEY `ventas_detalleventa_id_venta_id_55c94b1a` (`id_venta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_venta`
--

DROP TABLE IF EXISTS `ventas_venta`;
CREATE TABLE IF NOT EXISTS `ventas_venta` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `id_cliente_id` int NOT NULL,
  `id_usuario_id` int NOT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `ventas_venta_id_cliente_id_c7494267` (`id_cliente_id`),
  KEY `ventas_venta_id_usuario_id_3dfb99f4` (`id_usuario_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
