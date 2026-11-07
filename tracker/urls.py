from django.urls import path
from . import views
from .views import DeviceLocationCreateAPIView

urlpatterns = [
    path('api/location/update/', DeviceLocationCreateAPIView.as_view(), name='api-location-update'),
    path('location/', views.device_location, name='device_location'),
]
