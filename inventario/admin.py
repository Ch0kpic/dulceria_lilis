from django.contrib import admin
from .models import Category, Product, AlertRule, ProductAlertRule, Organization, Zone, Device, Measurement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sku', 'categoria')
    search_fields = ('nombre', 'sku')
    list_filter = ('categoria',)
    ordering = ('nombre',)
    list_select_related = ('categoria',)

@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'severidad', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('severidad',)
    ordering = ('severidad', 'nombre')

@admin.register(ProductAlertRule)
class ProductAlertRuleAdmin(admin.ModelAdmin):
    list_display = ('producto', 'regla_alerta', 'umbral_min', 'umbral_max')
    list_filter = ('regla_alerta__severidad',)
    search_fields = ('producto__nombre', 'regla_alerta__nombre')
    ordering = ('producto',)
    list_select_related = ('producto', 'regla_alerta')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'organizacion', 'descripcion')
    search_fields = ('nombre', 'organizacion__nombre')
    list_filter = ('organizacion',)
    ordering = ('organizacion', 'nombre')
    list_select_related = ('organizacion',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'zona', 'serial', 'estado')
    search_fields = ('nombre', 'serial', 'zona__nombre')
    list_filter = ('zona__organizacion', 'estado')
    ordering = ('zona', 'nombre')
    list_select_related = ('zona',)

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'valor', 'fecha')
    search_fields = ('dispositivo__nombre', 'dispositivo__serial')
    list_filter = ('dispositivo__zona__organizacion',)
    ordering = ('-fecha',)
    list_select_related = ('dispositivo',)
    date_hierarchy = 'fecha'
