from django.urls import path
from . import views

app_name = 'solicitudes_compra'

urlpatterns = [
    path('', views.lista_solicitudes, name='lista'),
    path('crear/', views.crear_solicitud, name='crear'),
    path('detalle/<int:id_solicitud>/', views.detalle_solicitud, name='detalle'),
    path('aprobar/<int:id_solicitud>/', views.aprobar_solicitud, name='aprobar'),
]