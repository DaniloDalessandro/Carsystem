from django.contrib import admin
from cars.models import Car,Brand

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand_name', 'brand_tipo', 'brand_categoria', 'factory_year', 'model_year', 'value')

    def brand_name(self, obj):
        return obj.brand.name
    brand_name.short_description = 'Brand Name'

    def brand_tipo(self, obj):
        return obj.brand.tipo
    brand_tipo.short_description = 'Brand Tipo'

    def brand_categoria(self, obj):
        return obj.brand.categoria
    brand_categoria.short_description = 'Brand Categoria'

admin.site.register(Brand)
admin.site.register(Car, CarAdmin)