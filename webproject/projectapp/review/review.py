from django.db import models
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django.core.validators import MinValueValidator, MaxValueValidator
from projectapp.customer import Customer
from projectapp.service import Service


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.PROTECT)
    services = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='reviews')
    rating = PositiveIntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    message = TextField(max_length=500)

    class Meta:
        ordering = ('rating',)