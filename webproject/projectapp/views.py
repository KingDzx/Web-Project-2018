from django.shortcuts import render
from rest_framework import viewsets
#from django.contrib.auth.models import User
from .customer import Customer, CustomerSerializer
from .worker import Worker
from .service import Service, ServiceSerializer
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def cat(request):

    categories = Service.objects.values()

    for line in categories:
        print (line['service_type'])

    return render(request, 'categories/categories.html', {'cat':categories})


def home(request):

    return render(request, 'homepage/home.html')