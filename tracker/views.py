from rest_framework import generics, permissions
from django.shortcuts import render
from .models import DeviceLocation
from .serializers import DeviceLocationSerializer

class DeviceLocationCreateAPIView(generics.CreateAPIView):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationSerializer
    permission_classes = [permissions.AllowAny]  # Hapa iwe permissions (yenye s)

def device_location(request):
    query = request.GET.get('device_name', '')
    location = None
    
    if query:
        location = DeviceLocation.objects.filter(device__icontains=query).order_by('-timestamp').first()
        
    context = {
        'location': location,
        'query': query
    }
    return render(request, 'tracker/location.html', context)
