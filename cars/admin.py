from django.contrib import admin
from cars.models import Car, Brand



class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'mileage', 'color', 'engine',)
    search_fields = ('model', 'brand', 'factory_year', 'model_year','plate', 'mileage', 'color', 'engine',)
    list_filter = ('factory_year', 'model_year','plate', 'mileage', 'color', 'engine',)



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
