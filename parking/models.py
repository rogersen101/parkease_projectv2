from django.db import models

# Create your models here.
class Vehicle(models.Model):
        VEHICLE_TYPES = [
                ('truck','Truck'),
                ('car', 'Personal Car'),
                ('taxi', 'Taxi'),
                ('coaster', 'Coaster'),
                ('boda', 'Boda-boda'),
        ]

        driver_name = models.CharField(max_length=150)
        vehicle_type = models.CharField(max_length=30, choices=VEHICLE_TYPES)
        number_plate = models.CharField(max_length=10)
        model_color = models.CharField(max_length=100)
        phone = models.CharField(max_length=15)
        nin = models.CharField(max_length=20, blank=True, null=True)
        arrival_time = models.DateTimeField()
        status = models.CharField(max_length=20, default='parked')

        def __str__(self):
                return self.number_plate


