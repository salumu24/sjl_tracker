from rest_framework import serializers
from .models import DeviceLocation

class DeviceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        fields = ['device', 'latitude', 'longitude', 'accuracy', 'recorded_at']
