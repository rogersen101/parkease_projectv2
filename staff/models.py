from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    ROLES = [('PARKING ATTENDANT','Parking Attendant'), ('SECTION MANAGER','Section Manager'), ('SYSTEM ADMIN','System Admin')]
    role = models.CharField(max_length=50, choices=ROLES)

    def __str__(self):
        return self.username
    
