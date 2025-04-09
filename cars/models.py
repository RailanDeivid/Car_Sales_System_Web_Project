from django.db import models



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    engine = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.model

    def formatted_value(self):
        if self.value is not None:
            return f'R$ {self.value:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')
        return 'R$ 0,00'

    def formatted_mileage(self):
        if self.mileage is not None:
            return f'{self.mileage:,}'.replace(',', '.')
        return '0'

