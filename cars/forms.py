from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 5000:
            self.add_error('value', 'O valor deve ser maior que R$ 5.000,00')
        return value