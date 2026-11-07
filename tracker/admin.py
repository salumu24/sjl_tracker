from django.contrib import admin
from .models import Device, DeviceLocation

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'serial_number', 'status', 'owner')
    list_filter = ('status', 'device_type')
    search_fields = ('device_name', 'serial_number', 'owner__username')


@admin.register(DeviceLocation)
class DeviceLocationAdmin(admin.ModelAdmin):

    list_display = (
          'device',
          'latitude',
          'longitude',
          'accuracy',
          'recorded_at',
    )

    list_filter = ('recorded_at',)

    search_fields = ('device__device_name',)

    readonly_fields = ('recorded_at',)


