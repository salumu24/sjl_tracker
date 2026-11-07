
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
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(-90),
            MaxValueValidator(90),
        ]
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180),
        ]
    )
    accuracy = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    recorded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.device.device_name} - {self.recorded_at}"
