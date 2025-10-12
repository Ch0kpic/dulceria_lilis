from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', login_required(views.home), name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('productos/', login_required(views.productos_view), name='productos'),
    path('productos/agregar/', login_required(views.agregar_producto), name='agregar_producto'),
    path('productos/editar/<int:producto_id>/', login_required(views.editar_producto), name='editar_producto'),
    path('inventarios/', login_required(views.inventarios_view), name='inventarios'),
    path('inventarios/agregar/', login_required(views.agregar_inventario), name='agregar_inventario'),
    path('inventarios/editar/<int:inventario_id>/', login_required(views.editar_inventario), name='editar_inventario'),
    path('proveedores/', login_required(views.proveedores_view), name='proveedores'),
    path('ventas/', login_required(views.ventas_view), name='ventas'),
]
