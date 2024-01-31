from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'car_type', 'battery_capacity', 'fuel_efficiency']

    def clean(self):
        cleaned_data = super().clean()
        car_type = cleaned_data.get('car_type')
        battery_capacity = cleaned_data.get('battery_capacity')
        fuel_efficiency = cleaned_data.get('fuel_efficiency')

        if car_type == 'Electric' and not battery_capacity:
            raise forms.ValidationError('Battery capacity is required for electric cars.')
        
        if car_type == 'Gas' and not fuel_efficiency:
            raise forms.ValidationError('Fuel efficiency is required for gas cars.')
