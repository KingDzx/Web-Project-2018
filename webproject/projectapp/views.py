from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .customer import Customer, CustomerSerializer
from .worker import Worker, WorkerSerializer
from .service import Service, ServiceSerializer
from .review import Review, ReviewSerializer
from django.views import View
from .forms import ServiceForm, UserForm
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
        services = Service.objects.all()
        #for line in services:
            #print(line['service'])
        return render(request, 'webpage/index.html', {'services':services})

class vewSer(View):
    def get(self,request):
        services = Service.objects.all()
        return render(request, 'webpage/browseServices.html', {'services':services})

class reView(View):
    def get(self,request):
        service = Service.objects.all()
        rev = Review.objects.all()
        #for line in rev:
            #print()
            #print(line['services'])
            #print(line['rating'])
            #print(line['message'])
        return render(request, 'webpage/browseReviews.html', {'review':rev})

class creUser(View):
    def get(self,request):
        return render(request, 'webpage/form.html')

class creSer(View):
    def get(self,request):
        form = ServiceForm()
        return render(request, 'webpage/registerServiceForm.html',{'form':form})

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
                return HttpResponseRedirect("/home")
        return render(request, 'webpage/registerServiceForm.html',{'form':form})

class getCategoryServices(View):
    def get(self,request):
        data = request.GET['category']
        services = Service.objects.filter(service = data)
        return render(request, 'webpage/catListing.html',{'services':services})

class getService(View):
    def get(self,request):
        data = request.GET['id']
        service = Service.objects.filter(id = data)
        return render(request, 'webpage/service.html',{'service':service})

class UserFormView(View):

    form_class = UserForm
    template_name = 'webpage/form.html'

    #Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.username = username
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return redirect('/home')

        return render(request, self.template_name, {'form': form})