from django.forms import ModelForm
from .service import Service
from django.contrib.auth.models import User
from django import forms

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ()