from django.forms import ModelForm
from .service import Service
from .review import Review
from django.contrib.auth.models import User
from django import forms

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ()