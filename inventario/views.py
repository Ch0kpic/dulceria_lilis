from django.shortcuts import render
from .models import Product

def dashboard_productos(request):
    productos = Product.objects.select_related('categoria').all()
    return render(request, 'inventario/dashboard_productos.html', {'productos': productos})
