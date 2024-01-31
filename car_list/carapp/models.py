from django.db import models

class Car(models.Model):
    ELECTRIC = 'Electric'
    GAS = 'Gas'
    CAR_TYPES = [
        (ELECTRIC, 'Electric'),
        (GAS, 'Gas'),
    ]

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    battery_capacity = models.IntegerField(null=True, blank=True)
    fuel_efficiency = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.name} {self.model}"
