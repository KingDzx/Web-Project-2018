from django.db import models
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import TextField

class Service(models.Model):
    service_type = (
        ("Appliance Repair","Appliance Repair"),
        ("Door Installation","Door Installation"),
        ("Electrician","Electrician"),
        ("Flooring","Flooring"),
        ("Upholstery","Upholstery"),
        ("Garage","Garage"),
        ("Home Security System","Home Security System"),
        ("Interior Design","Interior Design"),
        ("Landscaping","Landscaping"),
        ("Lighting Installation","Lighting Installation"),
        ("Moving","Moving"),
        ("Pest Control","Pest Control"),
        ("Plumber","Plumber"),
        ("Roofing","Roofing"),
        ("Auto","Auto"),
        ("Auto Body Repair","Auto Body Repair"),
        ("Auto Repair","Auto Repair"),
        ("Auto Service","Auto Service"),
        ("Health","Health"),
        ("Chiropractor","Chiropractor"),
        ("Counseling & Mental Health","Counseling & Mental Health"),
        ("Dentistry","Dentistry"),
        ("Dermatology","Dermatology"),
        ("Eye Care","Eye Care"),
        ("Fitness & Weight Management","Fitness & Weight Management"),
        ("Health Care Facility","Health Care Facility"),
        ("Home Health Care","Home Health Care"),
        ("Medical Specialist","Medical Specialist"),
        ("Pets","Pets"),
        ("Pet Care & Health Services","Pet Care & Health Services"),
        ("Finance Advising","Finance Advising"),
        ("Transportation","Transportation"),
        ("Wedding Planning","Wedding Planning"),
    )
    service = CharField(max_length = 100, choices=service_type, default = "Appliance Repair")
    name = CharField(max_length = 150)
    address = TextField(max_length = 200)
    description = TextField(max_length = 250)

    class Meta:
        ordering = ('name',)
