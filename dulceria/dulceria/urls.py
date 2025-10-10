"""
URL configuration for dulceria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .admin_custom import role_based_admin_site

urlpatterns = [
    # Admin personalizado basado en roles
    path('admin/', role_based_admin_site.urls),
    
    # URLs de la aplicación
    path('', lambda request: redirect('login')),
    path('', include('authentication.urls')),
    path('productos/', include('productos.urls')),
    path('inventario/', include('inventario.urls')),
    path('solicitudes-compra/', include('solicitudes_compra.urls')),
]
