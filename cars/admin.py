from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'model_year',)
    list_filter = ('factory_year', 'model_year')


admin.site.register(Car, CarAdmin)