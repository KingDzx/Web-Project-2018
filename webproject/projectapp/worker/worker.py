from django.db import models
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import TextField
from django.db.models import DateTimeField

class Worker(models.Model):
    first_name = CharField(max_length = 100)
    last_name = CharField(max_length = 100)
    username = CharField(max_length = 100)
    password = CharField(max_length = 100)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('first_name', 'last_name', 'created')