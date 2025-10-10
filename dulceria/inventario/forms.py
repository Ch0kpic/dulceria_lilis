from django import forms
from .models import Inventario
from productos.models import Producto

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['id_producto', 'cantidad_actual', 'ubicacion', 'stock_minimo', 'stock_maximo']
        widgets = {
            'id_producto': forms.Select(attrs={
                'class': 'form-control'
            }),
            'cantidad_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Estante A1, Bodega Principal, etc.'
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'value': '5'
            }),
            'stock_maximo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'value': '100'
            })
        }
        labels = {
            'id_producto': 'Producto',
            'cantidad_actual': 'Cantidad Actual',
            'ubicacion': 'Ubicación',
            'stock_minimo': 'Stock Mínimo',
            'stock_maximo': 'Stock Máximo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo productos activos
        self.fields['id_producto'].queryset = Producto.objects.filter(activo=True).order_by('nombre')
        
        # Hacer todos los campos requeridos
        for field in self.fields.values():
            field.required = True