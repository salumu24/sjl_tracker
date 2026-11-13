from django.contrib import admin
from .models import DeviceLocation

@admin.register(DeviceLocation)
class DeviceLocationAdmin(admin.ModelAdmin):
    list_display = ('device', 'latitude', 'longitude', 'taifa', 'mkoa', 'wilaya', 'kata', 'mtaa', 'timestamp')
    list_filter = ('mkoa', 'wilaya', 'taifa', 'timestamp')
    search_fields = ('device', 'mkoa', 'wilaya', 'kata', 'mtaa')
    readonly_fields = ('timestamp',)
