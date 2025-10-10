from django import forms
from django.forms import inlineformset_factory
from .models import SolicitudCompra, DetalleSolicitudCompra
from productos.models import Producto
from proveedores.models import Proveedor

class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        fields = ['proveedor', 'prioridad', 'fecha_necesaria', 'observaciones']
        widgets = {
            'proveedor': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_necesaria': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proveedor'].queryset = Proveedor.objects.all()
        self.fields['fecha_necesaria'].required = True

class DetalleSolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleSolicitudCompra
        fields = ['producto', 'cantidad_solicitada', 'precio_estimado', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'form-select producto-select',
                'required': True
            }),
            'cantidad_solicitada': forms.NumberInput(attrs={
                'class': 'form-control cantidad-input',
                'min': '1',
                'step': '1'
            }),
            'precio_estimado': forms.NumberInput(attrs={
                'class': 'form-control precio-input',
                'min': '0.01',
                'step': '0.01'
            }),
            'observaciones': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones del producto...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(activo=True)
        self.fields['cantidad_solicitada'].required = True
        self.fields['precio_estimado'].required = True

# Formset para manejar múltiples detalles
DetalleSolicitudFormSet = inlineformset_factory(
    SolicitudCompra,
    DetalleSolicitudCompra,
    form=DetalleSolicitudCompraForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True
)