from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.lista_inventario, name='lista'),
    path('crear/', views.crear_inventario, name='crear'),
    path('<int:pk>/', views.detalle_inventario, name='detalle'),
    path('<int:pk>/editar/', views.editar_inventario, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_inventario, name='eliminar'),
    path('producto/<int:producto_id>/', views.inventario_por_producto, name='por_producto'),
]