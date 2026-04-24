from django.db import models
import uuid

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
        arrival_time = models.DateTimeField(auto_now_add=True)
        status = models.CharField(max_length=20, default='parked')

        def __str__(self):
                return self.number_plate
        
       


class Payment(models.Model):
    vehicle = models.ForeignKey('parking.Vehicle', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_number = models.CharField(max_length=20, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = "RCPT-" + str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.receipt_number
    
class SignOut(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=100)
    receipt_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    nin = models.CharField(max_length=20)
    signout_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.number_plate


