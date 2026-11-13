
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Device(models.Model):
    DEVICE_TYPES = [
        ('Smartphone', 'Smartphone'),
        ('Laptop', 'Laptop'),
        ('Tablet', 'Tablet'),
        ('Desktop', 'Desktop'),
    ]
    
    STATUS_CHOICES = [
        ('REGISTERED', 'Registered'),
        ('LOST', 'Lost'),
        ('RECOVERED', 'Recovered'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPES)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REGISTERED')

    def _str_(self):
        return self.device_name


class DeviceLocation(models.Model):
    device = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    # Sehemu mpya za eneo la kijiografia
    taifa = models.CharField(max_length=100, blank=True, null=True)
    mkoa = models.CharField(max_length=100, blank=True, null=True)
    wilaya = models.CharField(max_length=100, blank=True, null=True)
    kata = models.CharField(max_length=100, blank=True, null=True)
    mtaa = models.CharField(max_length=100, blank=True, null=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.device} - {self.mkoa}, {self.wilaya}"
