from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from .models import DeviceLocation
from .serializers import DeviceLocationSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Hii inazima ukaguzi wa CSRF kwenye DRF

def home(request):
    return HttpResponse("Welcome to SJL tracker")

def device_location(request):
    latest_location = DeviceLocation.objects.last()
    context = {
        'location': latest_location
    }
    return render(request, 'tracker/location.html', context)

class DeviceLocationCreateAPIView(generics.CreateAPIView):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
