from django.db import models

# Create your models here.
class TyreService(models.Model):
    SERVICE_TYPES = [
        ('pressure', 'Pressure'),
        ('puncture', 'Puncture Fix'),
        ('valve', 'Valve'),
    ]

    vehicle = models.ForeignKey('parking.Vehicle', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)