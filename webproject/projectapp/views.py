from django.shortcuts import render
from rest_framework import viewsets
#from django.contrib.auth.models import User
from .customer import Customer
from .worker import Worker
from .service import Service, ServiceSerializer
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer