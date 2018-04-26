from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from rest_framework import viewsets
from .customer import Customer, CustomerSerializer
from .worker import Worker, WorkerSerializer
from .service import Service, ServiceSerializer
from .review import Review, ReviewSerializer
from django.views import View
from .forms import ServiceForm
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class cat(View):
    def get(self,request):
        categories = Service.objects.values()
        for line in categories:
            print(line['service'])
        return render(request, 'categories/categories.html', {'cat':categories})

class creSer(View):
    def get(self,request):
        form = ServiceForm()
        return render(request, 'createSer/createSer.html',{'form':form})

    def post(self,request):
        form = ServiceForm()
        if request.method =='POST':
            form = ServiceForm(request.POST, request.FILES)
            if form.is_valid():
                service = Service
                service.name = form.cleaned_data['name']
                service.service = form.cleaned_data['service']
                service.address = form.cleaned_data['address']
                service.description = form.cleaned_data['description']
                form.save()
                return HttpResponseRedirect("/?openr=cat&res=true")
        return render(request, 'createSer/createSer.html')
            